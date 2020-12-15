def test_print_message(capsys):
    try:
        from .. import task as t
        t.print_message()
        out, err = capsys.readouterr()
        print(f"The output: {type(out)} and the error: {type(err)}")
        if out == 'look at me I am coding\n':
            assert "look at me I am coding" == "a different message", 'You should change the message'
        print("\n")
        print(out)
    except SyntaxError:
        assert ('An invalid syntax' == 'Some words surrounded by quotes'), "Check your message for quotation marks"