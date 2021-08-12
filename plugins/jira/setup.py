# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="jira-rapid7-plugin",
      version="6.1.0",
      description="Automate the creation, search and management of issues, users, and alerting for Jira Software, Jira Server, and Jira ServiceDesk",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_jira']
      )
