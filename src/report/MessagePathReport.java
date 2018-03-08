/*
 * Implemented by Micah Terrell
 */
package report;

import core.DTNHost;
import core.Message;
import core.MessageListener;
import java.util.concurrent.LinkedBlockingQueue;

/**
 * Reports information about all created messages. Messages created during
 * the warm up period are ignored.
 * For output syntax, see {@link #HEADER}.
 */
public class MessagePathReport extends Report implements MessageListener {
	public static String HEADER = "TODO: Implement header";

	private LinkedBlockingQueue<Message> messages;
	/**
	 * Constructor.
	 */
	public MessagePathReport() {
		init();
	}

	@Override
	public void init() {
		super.init();
		write(HEADER);
	}


	public void messageDeleted(Message m, DTNHost where, boolean dropped) {
		if (isWarmup()) {
			return;
		}

		try {
			String messageStats = m.getId() + "," + m.getFrom() + "," + m.getTo() + ",";

			for(int i = 0; i < m.getHops().size(); i++) {
				messageStats = messageStats + m.getHops().get(i).getName();
				if(i + 1 != m.getHops().size()) {
					messageStats = messageStats + ">";
				}
			}
			write(messageStats);
		} catch(Exception e) {
			write("Exception Thrown\n");
		}
		
	}

	public void messageTransferred(Message m, DTNHost from, DTNHost to, boolean firstDelivery) {
		if (isWarmup() || !firstDelivery) {
			return;
		}

		try {
			String messageStats = m.getId() + "," + m.getFrom() + "," + m.getTo() + ",";

			for(int i = 0; i < m.getHops().size(); i++) {
				messageStats = messageStats + m.getHops().get(i).getName();
				if(i + 1 != m.getHops().size()) {
					messageStats = messageStats + ">";
				}
			}
			write(messageStats);
		} catch(Exception e) {
			write("Exception Thrown\n");
		}
	}

	// nothing to implement for the rest
	public void newMessage(Message m) {}
	public void messageTransferAborted(Message m, DTNHost from, DTNHost to) {}
	public void messageTransferStarted(Message m, DTNHost from, DTNHost to) {}

	@Override
	public void done() {
		super.done();	
	}
}
