# coding: utf8
import sublime
import sublime_plugin


class LogCommandsCommand(sublime_plugin.TextCommand):
    def run(self, edit, set):
        sublime.log_commands(set)
