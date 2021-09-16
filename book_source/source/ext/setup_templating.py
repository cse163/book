# Kind of annoying bug, but we can't include our own templates_path in the config
# As it overwrites the one set up by Jupyter Book. Have  to add it here instead
# For some reason, the google_analytics_id property you can set in the theme doesn't work


def setup(app):
    # Add our templates directory to the templates_path
    app.config.templates_path.insert(0, "_templates")

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
