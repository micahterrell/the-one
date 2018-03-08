package routing;

import core.Settings;

public class StaticPriorityRouter extends ClassPriorityRouter {

	/**
	 * Constructor. Creates a new message router based on the settings in
	 * the given Settings object.
	 * @param s The settings object
	 */
	public StaticPriorityRouter(Settings s) {
		super(s);
	}

	/**
	 * Copyconstructor.
	 * @param r The router prototype where setting values are copied from
	 */
	protected StaticPriorityRouter(StaticPriorityRouter r) {
		super(r);
	}

	@Override
	public int getRouterClassPriority() {
		return -999;  //TODO: Hardcoded for now
	}

	@Override
	public MessageRouter replicate() {
		return new StaticPriorityRouter(this);
	}
}