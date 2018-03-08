package routing;

import core.Settings;

public class DronePriorityRouter extends ClassPriorityRouter {

	/**
	 * Constructor. Creates a new message router based on the settings in
	 * the given Settings object.
	 * @param s The settings object
	 */
	public DronePriorityRouter(Settings s) {
		super(s);
	}

	/**
	 * Copyconstructor.
	 * @param r The router prototype where setting values are copied from
	 */
	protected DronePriorityRouter(DronePriorityRouter r) {
		super(r);
	}

	@Override
	public int getRouterClassPriority() {
		return 2; //TODO: Hardcoded for now
	}

	@Override
	public MessageRouter replicate() {
		return new DronePriorityRouter(this);
	}
}