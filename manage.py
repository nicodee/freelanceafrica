#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freelanceproject.settings")

    from django.core.management import execute_from_command_line
    import freelanceproject.startup as startup
    import freelanceapp.skillset as skillset
    try:
    	startup.run()
    	skillset.create_base_skills()
    except:
    	pass

    execute_from_command_line(sys.argv)
