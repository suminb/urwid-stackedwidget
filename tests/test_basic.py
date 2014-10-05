from urwid_stackedwidget import StackedWidget
import urwid
import pytest


# TODO: Test mouse_event()

def stringify(raw):
    """
    :param raw: A list of byte strings (raw output from widget.text)
    """
    return '\n'.join(map(str, raw))


@pytest.fixture
def stacked_widget1():
    stacked_widget = StackedWidget()
    stacked_widget.push_widget(
        urwid.Filler(urwid.Text('The first widget')))
    stacked_widget.push_widget(
        urwid.Filler(urwid.Text('The second widget')))
    stacked_widget.push_widget(
        urwid.Filler(urwid.Text('The third widget')))

    return stacked_widget


def test_properties(stacked_widget1):
    stacked_widget0 = StackedWidget()

    assert stacked_widget0.selectable
    assert stacked_widget0.widget_count == 0
    assert stacked_widget0.current_widget is None

    assert stacked_widget1.selectable
    assert stacked_widget1.widget_count == 3
    assert stacked_widget1.current_widget is not None


def test_pop_and_push(stacked_widget1):
    assert stacked_widget1.widget_count == 3

    stacked_widget1.pop_widget()
    assert stacked_widget1.widget_count == 2

    stacked_widget1.push_widget(urwid.Text('This is a new widget'))
    assert stacked_widget1.widget_count == 3

    stacked_widget1.insert_widget(0, urwid.Text('This is a new widget'))
    assert stacked_widget1.widget_count == 4


def test_show_next_widget(stacked_widget1):
    size = (20, 2)

    canvas = stacked_widget1.render(size)
    assert 'first' in stringify(canvas.text)

    stacked_widget1.show_next_widget()
    canvas = stacked_widget1.render(size)
    assert 'second' in stringify(canvas.text)

    stacked_widget1.show_next_widget()
    canvas = stacked_widget1.render(size)
    assert 'third' in stringify(canvas.text)

    # Shall wrap-around
    stacked_widget1.show_next_widget()
    canvas = stacked_widget1.render(size)
    assert 'first' in stringify(canvas.text)


def test_show_previous_widget(stacked_widget1):
    size = (20, 2)

    canvas = stacked_widget1.render(size)
    assert 'first' in stringify(canvas.text)

    stacked_widget1.show_previous_widget()
    canvas = stacked_widget1.render(size)
    assert 'third' in stringify(canvas.text)

    stacked_widget1.show_previous_widget()
    canvas = stacked_widget1.render(size)
    assert 'second' in stringify(canvas.text)

    stacked_widget1.show_previous_widget()
    canvas = stacked_widget1.render(size)
    assert 'first' in stringify(canvas.text)
