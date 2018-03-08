package routing;

import core.Settings;

public class VehiclePriorityRouter extends ClassPriorityRouter {

	/**
	 * Constructor. Creates a new message router based on the settings in
	 * the given Settings object.
	 * @param s The settings object
	 */
	public VehiclePriorityRouter(Settings s) {
		super(s);
	}

	/**
	 * Copyconstructor.
	 * @param r The router prototype where setting values are copied from
	 */
	protected VehiclePriorityRouter(VehiclePriorityRouter r) {
		super(r);
	}

	@Override
	public int getRouterClassPriority() {
		return 1;  //TODO: Hardcoded for now
	}

	@Override
	public MessageRouter replicate() {
		return new VehiclePriorityRouter(this);
	}
}