# -*- coding: utf-8 -*-
import urwid

__author__ = 'Sumin Byeon'
__version__ = '0.1.3'
__all__ = ['StackedWidget']


class StackedWidget(urwid.Widget):
    """A widget container that presents one child widget at a time."""

    #: A list containing all widgets
    widgets = []

    #: An index of the current widget
    current = 0

    def __init__(self):
        self.widgets = []
        self.current = 0

    def add_widget(self, widget):
        # Deprecated
        self.push_widget(widget)

    def push_widget(self, widget):
        """Appends a widget at the end of the list."""
        self.widgets.append(widget)

    def insert_widget(self, index, widget):
        """Inserts a widget at a given index."""
        self.widgets.insert(index, widget)

    def pop_widget(self):
        """Retrieves and removes the last widget (with the maximum index)."""
        n = len(self.widgets)
        assert n > 0

        widget = self.widgets.pop()
        if self.current == n - 1:
            self.current -= 1

        self._invalidate()

        return widget

    def show_widget(self, index):
        assert 0 <= index < len(self.widgets)
        self.current = index
        self._invalidate()

    def show_next_widget(self):
        n = len(self.widgets)
        assert n > 0

        self.current = (self.current + 1) % n
        self._invalidate()

    def show_previous_widget(self):
        n = len(self.widgets)
        assert n > 0

        self.current = (self.current - 1 + n) % n
        self._invalidate()

    @property
    def widget_count(self):
        """The function name is pretty much self-explanatory."""
        return len(self.widgets)

    @property
    def current_widget(self):
        """Returns a widget that is currently being rendered. If the widget
        list is empty, it returns None."""
        if self.widget_count > 0:
            return self.widgets[self.current]
        else:
            return None

    def selectable(self):
        """It appears ``selectable()`` must return ``True`` in order to get any
        key input."""

        return True

    def render(self, size, focus=False):
        assert self.current_widget is not None

        return self.current_widget.render(size, focus)

    def keypress(self, size, key):
        """Passes key inputs to the current widget. If the current widget is
        ``None`` then it returns the given key input so that
        ``unhandled_input`` function can handle it."""

        if self.current_widget is not None:
            return self.current_widget.keypress(size, key)
        else:
            return key

    def mouse_event(self, size, event, button, col, row, focus):
        if self.current_widget is not None:
            return self.current_widget.mouse_event(
                    size, event, button, col, row, focus)
        else:
            return key
