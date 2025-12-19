def build_context(activity):
    """Return a minimal context dict for the given activity."""
    return {"activity_id": getattr(activity, "id", None)}
