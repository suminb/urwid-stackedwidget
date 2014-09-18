from urwidext_stackedwidget import StackedWidget
import urwid

stacked_widget = StackedWidget()


def keypress(key):
    if key in 'qQ':
        raise urwid.ExitMainLoop()
    elif key == 'left':
        n = stacked_widget.widget_count
        stacked_widget.show_widget((stacked_widget.current - 1 + n) % n)
    elif key == 'right':
        n = stacked_widget.widget_count
        stacked_widget.show_widget((stacked_widget.current + 1) % n)



def main():
    stacked_widget.push_widget(
        urwid.Filler(urwid.Text('The first widget')))
    stacked_widget.push_widget(
        urwid.Filler(urwid.Text('The second widget')))
    stacked_widget.push_widget(
        urwid.Filler(urwid.Text('The third widget')))

    loop = urwid.MainLoop(stacked_widget, unhandled_input=keypress)

    try:
        loop.run()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
