/*
 * Copyright 2010 Aalto University, ComNet
 * Released under GPLv3. See LICENSE.txt for details.
 */
package routing;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import routing.util.RoutingInfo;

import util.Tuple;

import core.Connection;
import core.DTNHost;
import core.Message;
import core.Settings;
import core.SimClock;

/**
 * Implementation of PRoPHET router as described in
 * <I>Probabilistic routing in intermittently connected networks</I> by
 * Anders Lindgren et al.
 */
public abstract class ClassPriorityRouter extends ActiveRouter {
	
	/**
	 * Constructor. Creates a new message router based on the settings in
	 * the given Settings object.
	 * @param s The settings object
	 */
	public ClassPriorityRouter(Settings s) {
		super(s);
	}

	/**
	 * Copyconstructor.
	 * @param r The router prototype where setting values are copied from
	 */
	protected ClassPriorityRouter(ClassPriorityRouter r) {
		super(r);
	}


	//Force child classes to define their router class priority
	public abstract int getRouterClassPriority();

	@Override
	public void update() {
		super.update();
		if (!canStartTransfer() || isTransferring()) {
			return; // nothing to transfer or is currently transferring
		}

		// try messages that could be delivered to final recipient
		if (exchangeDeliverableMessages() != null) {
			return;
		}

		tryOtherMessages();
	}



	/**
	 * Tries to send all other messages to all connected hosts ordered by
	 * their delivery probability
	 * @return The return value of {@link #tryMessagesForConnected(List)}
	 */
	private Tuple<Message, Connection> tryOtherMessages() {
		//TODO:CHECKME THIS IS THE METHOD TO CHANGE
		List<Tuple<Message, Connection>> messages = new ArrayList<Tuple<Message, Connection>>();

		Collection<Message> msgCollection = getMessageCollection();

		/* for all connected hosts collect all messages that have a higher
		   probability of delivery by the other host */
		for (Connection con : getConnections()) {
			DTNHost otherHost = con.getOtherNode(getHost());
			ClassPriorityRouter otherRouter = (ClassPriorityRouter) otherHost.getRouter();

			if (otherRouter.isTransferring()) {
				continue; // skip hosts that are transferring
			}

			for (Message m : msgCollection) {
				if (otherRouter.hasMessage(m.getId())) {
					continue; // skip messages that the other one has
				}

				messages.add(new Tuple<Message, Connection>(m,con));	
			}
		}

		if (messages.size() == 0) {
			return null;
		}

		// sort the message-connection tuples
		Collections.sort(messages, new ConnectionPriorityComparator());
		return tryMessagesForConnected(messages);	// try to send messages
	}

	/**
	 * Comparator for Message-Connection-Tuples that orders the tuples by
	 * their delivery probability by the host on the other side of the
	 * connection (GRTRMax)
	 */
	private class ConnectionPriorityComparator implements Comparator <Tuple<Message, Connection>> {
		public int compare(Tuple<Message, Connection> tuple1, Tuple<Message, Connection> tuple2) {
			//Compare the priority of each connect by getting the router type routing priority.
			DTNHost hostOne = tuple1.getValue().getOtherNode(getHost());
			ClassPriorityRouter routerOne = (ClassPriorityRouter) hostOne.getRouter();
			
			DTNHost hostTwo = tuple2.getValue().getOtherNode(getHost());
			ClassPriorityRouter routerTwo = (ClassPriorityRouter) hostTwo.getRouter();

			if(routerOne.getRouterClassPriority() > routerTwo.getRouterClassPriority()) {
				return 1;
			} else if(routerOne.getRouterClassPriority() == routerTwo.getRouterClassPriority()) {
				return 0;
			} else {
				return -1;
			}
		}
	}


}
