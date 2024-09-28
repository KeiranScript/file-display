from pygments.style import Style
from pygments.token import Token


class CustomStyle(Style):
    background_color = "#282c34"
    default_style = ""

    styles = {
        Token.Comment: "italic #5c6370",
        Token.Keyword: "bold #c678dd",
        Token.Name: "#e06c75",
        Token.String: "#98c379",
        Token.Number: "#d19a66",
        Token.Operator: "#61afef",
        Token.Punctuation: "#abb2bf",
        Token.Function: "#61afef",
        Token.Class: "#c678dd",
        Token.Builtin: "#d19a66",
        Token.Exception: "#e06c75",
        Token.Namespace: "#e06c75",
        Token.Type: "#56b6c2",
        Token.Property: "#e06c75",
        Token.Constant: "#d19a66",
        Token.Function: "#61afef",
        Token.Method: "#61afef",
    }
