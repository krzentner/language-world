
'''[eod] [code]import os
import os.path

import sublime
import sublime_plugin
import subprocess

class MarkdownFormatterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		settings = view.settings()
		text = view.substr(sublime.Region(0, view.size()))

		# Use the markdown_preview_plus python binary from the user's 
		# settings or fallback on system python.
		binary = settings.get('markdown_preview_plus_python') or 'python'

		# Find the user's working directory or fallback on the project directory.
		cwd = settings.get('markdown_preview_plus_work_dir') or view.window().folders()[0]

		# Find the file.
		filepath = os.path.realpath(view.file_name())

		# Ensure the markdown preview plus is on the user's path.
		user_path = os.environ.get('PATH')
		if os.path.dirname(binary) not in user_path:
			user_path += os.pathsep + os.path.dirname(binary)
		env = os.environ.copy()
		env['PATH'] = user_path

		# Format the markdown.
		proc = subprocess.Popen([binary, os.path.join(os.path.dirname(__file__), 'markdown_preview_plus'), '--format-only'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, cwd=cwd)
		(out, err) = proc.communicate(text)

		# Set the formatted markdown.
		if proc.returncode == 0:
			view.replace(edit, sublime.Region(0, view.size()), out.decode('utf-8'))
		elif err:
			sublime.error_message(err.decode('utf-8'))[eod] [code]#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = RotatingFileHandler('data-uploader.log', maxBytes=1