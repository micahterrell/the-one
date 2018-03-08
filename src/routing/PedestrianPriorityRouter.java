package routing;

import core.Settings;

public class PedestrianPriorityRouter extends ClassPriorityRouter {

	/**
	 * Constructor. Creates a new message router based on the settings in
	 * the given Settings object.
	 * @param s The settings object
	 */
	public PedestrianPriorityRouter(Settings s) {
		super(s);
	}

	/**
	 * Copyconstructor.
	 * @param r The router prototype where setting values are copied from
	 */
	protected PedestrianPriorityRouter(PedestrianPriorityRouter r) {
		super(r);
	}

	@Override
	public int getRouterClassPriority() {
		return 0;  //TODO: Hardcoded for now
	}

	@Override
	public MessageRouter replicate() {
		return new PedestrianPriorityRouter(this);
	}
}