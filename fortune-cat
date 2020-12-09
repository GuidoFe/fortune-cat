#!/usr/bin/python3
import sys
import os
import re
import argparse
from io import StringIO

class CatConfig:
    def __init__(self):
        self.CAT=[  '  ∧＿∧',
                    ' ( ･ω･)',
                    '─∪────∪─',
                    ' OUTPUT ',
                    '━┯━━━━┯━',
                    ' |    |',
                    ' |    |',
                    '  U  U']
        # Top left and right corners
        self.TL_CORNER_CHAR = '┌'
        self.TR_CORNER_CHAR = '┒'

        # Bottom left and right corners
        self.BL_CORNER_CHAR = '┕'
        self.BR_CORNER_CHAR = '┛'

        # Left, right, top and bottom sign characters
        self.L_WALL = '│'
        self.R_WALL = '┃'
        self.TOP = '─'
        self.BOTTOM = '━'

        # Padding between the sign side and the input text
        self.TEXT_PADDING_SIDE = 3

        # Padding between the sign top or bottom and the input text
        self.TEXT_PADDING_VERTICAL = 1

        # Vertical padding of the entire drawing
        self.GLOBAL_PADDING = 2

        # Horizontal position of the cat relative to the sign.
        # Example 0 = left, 0.5 = center, 1 = right
        self.CAT_POS = 0.5

        # Horizontal position of the sign in the terminal.
        # Same as CAT_POS
        self.GLOBAL_POS = 0.5

        # Width of the drawing, box corners excluded
        self.CAT_WIDTH = 8
        self.OUTPUT_INDEX = 3

        # Length for a tab character
        self.TAB_LEN = 2

        # Force a maximum line length. 0 if the only limit is the terminal width

        self.FORCED_TEXT_WIDTH = 0

###############################################à

input = sys.stdin
catFile = None

def setConst(p, cat):
    if p.top_left is not None:
        cat.TL_CORNER_CHAR = p.top_left
    if p.top_right is not None:
        cat.TR_CORNER_CHAR = p.top_right
    if p.bottom_left is not None:
        cat.BL_CORNER_CHAR = p.bottom_left
    if p.bottom_right is not None:
        cat.BR_CORNER_CHAR = p.bottom_right
    if p.left is not None:
        cat.L_WALL = p.left
    if p.right is not None:
        cat.R_WALL = p.right
    if p.top is not None:
        cat.TOP = p.top
    if p.bottom is not None:
        cat.BOTTOM = p.bottom
    if p.text_padding_h is not None:
        cat.TEXT_PADDING_SIDE = p.text_padding_h
    if p.text_padding_v is not None:
        cat.TEXT_PADDING_VERTICAL = p.text_padding_v
    if p.padding is not None:
        cat.GLOBAL_PADDING = p.padding
    if p.cat_position is not None:
        cat.CAT_POS = p.cat_position
    if p.global_position is not None:
        cat.GLOBAL_POS = p.global_position
    if p.tab_length is not None:
        cat.TAB_LEN = p.tab_length
    if p.max_text_length is not None:
        cat.FORCED_TEXT_WIDTH = p.max_text_length

    if p.fortune is not None:
        global input
        input.flush()
        input = StringIO(p.fortune)
        input.seek(0)
    global catFile
    if p.drawing_file != None:
        catFile = p.drawing_file

def getOptions(args, cat):
    desc = ("Show a cat around a text.\n\n"
            "If you want to save the options in a config file, write them like\n"
            "you would do in the terminal, in a single line. Example: \n\n"
            "-p 3 --top _ -cp 0.3\n\n"
            "To specify a custom cat, write a file where:\n"
            "\t- the first line is the width of the drawing\n"
            "\t- lines that contains the top drawing\n"
            "\t- A line with \"OUTPUT\"\n"
            "\t- lines that contains the bottom drawing\n\n"
            "Example:\n\n"
            "8\n"
            "  ∧＿∧\n"
            " ( ･ω･)\n"
            "─∪────∪─\n"
            "OUTPUT\n"
            "━┯━━━━┯━\n"
            " ┆    ┆\n"
            " ┆    ┆\n"
            "  U  U\n\n"
            "You can also append the drawing directly in the config file,\n"
            "starting from the second line. Remember to specify the line length\n"
            "first.\n"
            "If the drawing is specified bot in the config and drawing files,\n"
            "only the cat in the drawing file will be considered")
    parser = argparse.ArgumentParser(description="Print a cat sneaking over your fortune quote", epilog=desc, formatter_class=argparse.RawDescriptionHelpFormatter)
    drawingGroup = parser.add_argument_group("Drawing options")
    textGroup = parser.add_argument_group("Text options")
    parser.add_argument("-d", "--drawing-file", type=argparse.FileType('r'), help="File with a custom cat/animal/thinghy")
    parser.add_argument("-c", "--config-file", type=argparse.FileType('r'), help="Custom config file.")
    drawingGroup.add_argument("-tl", "--top-left", help="Top left corner char")
    drawingGroup.add_argument("-tr", "--top-right", help="Top right corner char")
    drawingGroup.add_argument("-bl", "--bottom-left", help="Bottom left corner char")
    drawingGroup.add_argument("-br", "--bottom-right", help="Bottom right corner char")
    drawingGroup.add_argument("-l", "--left", help="Left box char")
    drawingGroup.add_argument("-r", "--right", help="Right box char")
    drawingGroup.add_argument("-t", "--top", help="Top box char")
    drawingGroup.add_argument("-b", "--bottom", help="Bottom box char")
    textGroup.add_argument("-tph", "--text-padding-h", type=int, help="Horizontal text padding")
    textGroup.add_argument("-tpv", "--text-padding-v", type=int, help="Vertical text padding")
    drawingGroup.add_argument("-p", "--padding", type=int, help="Vertical padding of the entire output")
    drawingGroup.add_argument("-cp", "--cat-position", type=float, help="Position from 0 to 1 of the cat relative to the box. 0 = all to the left, 1 = all to the right, 0.5 = center")
    drawingGroup.add_argument("-gp", "--global-position", type=float, help="Position like --cat-position, but of the entire output relative to the terminal")
    textGroup.add_argument("-tb", "--tab-length", type=int, help="How many spaces a tab in the input text should be. Default = 2")
    textGroup.add_argument("-mtl", "--max-text-length", type=int, help="Set a maximum length for the text. Default is 0, that means it will only adapt to the terminal")
    parser.add_argument('fortune', nargs='?', help="Forune string, if not passed via pipe")
    p=parser.parse_args(args)
    return p

def parseDrawing(f, cat):
    catLen = f.readline().strip()
    if len(catLen) > 0:
        cat.CAT_WIDTH = int(catLen)
        cat.CAT = []
        i = 0
        for line in f:
            line = line.replace("\n", "")
            if line.strip() == "OUTPUT":
                cat.OUTPUT_INDEX = i
                cat.CAT.append("")
            else:
                cat.CAT.append(line)
            i += 1
        if len(cat.CAT[len(cat.CAT)-1].strip()) == 0:
            cat.CAT.remove(len(cat.CAT)-1)

def main():
    global catFile
    global input
    cat = CatConfig()
    terminalWidth, terminalHeight = os.get_terminal_size()
    if len(sys.argv) > 1:
        parser = getOptions(sys.argv[1:], cat)
        configFile = parser.config_file
        if configFile != None:
            configOptions = configFile.readline().strip().split(" ")
            fileParser = getOptions(configOptions, cat)
            setConst(fileParser, cat)
            parseDrawing(configFile, cat)
        setConst(parser, cat)
        if catFile != None:
            parseDrawing(catFile, cat)
    maxTextLen = 0
    text = []
    maximumTextSpace = terminalWidth - cat.TEXT_PADDING_SIDE * 2 - 2
    if cat.FORCED_TEXT_WIDTH > 0 and maximumTextSpace > cat.FORCED_TEXT_WIDTH:
        maximumTextSpace = cat.FORCED_TEXT_WIDTH
    for line in input:
        line = line.replace("\n", "")
        line = line.replace("\t", " " * cat.TAB_LEN)

        # Many fortune quites have double spaces after a punctuation, idk why

        while True:
            el = re.search("[.?!)\"'¿]  \S", line)
            if el != None:
                index = el.start()
                line = line[:index+1] + line[index+2:]
            else:
                break

        if len(line) > maximumTextSpace:
            while len(line) > maximumTextSpace:
                index = maximumTextSpace - 1
                while index != 0 and line[index] != " ":
                    index -= 1
                if index == 0:
                    maxTextLen = maximumTextSpace
                    text.append(line[0:maximumTextSpace])
                    line = line[maximumTextSpace:]
                else:
                    maxTextLen = max(index, maxTextLen)
                    text.append(line[0:index])
                    line = line[index+1:]
            maxTextLen = max(maxTextLen, len(line))
            text.append(line)
        else:
            maxTextLen = max(maxTextLen, len(line))
            text.append(line)
    insideWidth = cat.TEXT_PADDING_SIDE * 2 + maxTextLen
    if maxTextLen + cat.TEXT_PADDING_SIDE * 2 < cat.CAT_WIDTH:
        insideWidth = cat.CAT_WIDTH
    globalTextPadding = round(terminalWidth * cat.GLOBAL_POS - (insideWidth + 2) / 2)
    if globalTextPadding < 0:
        globalTextPadding = 0
    if globalTextPadding + insideWidth + 2 > terminalWidth:
        globalTextPadding = terminalWidth - insideWidth - 2
    relativeCatPadding = round(insideWidth * cat.CAT_POS - cat.CAT_WIDTH / 2)
    if relativeCatPadding < 0:
        relativeCatPadding = 0
    if relativeCatPadding + cat.CAT_WIDTH > insideWidth:
        relativeCatPadding = insideWidth - cat.CAT_WIDTH
    globalCatPadding = globalTextPadding + 1 + relativeCatPadding
    globalTextSpaces = globalTextPadding * " "
    globalCatSpaces = globalCatPadding * " "
    for i in range(cat.GLOBAL_PADDING):
        print()
    for i in range(len(cat.CAT)):
        if i == cat.OUTPUT_INDEX:
            for j in range(cat.TEXT_PADDING_VERTICAL):
                print(globalTextSpaces + cat.L_WALL + insideWidth * " " + cat.R_WALL)
            for j in range(len(text)):
                rightPadding = insideWidth - cat.TEXT_PADDING_SIDE - len(text[j])
                print(globalTextSpaces + cat.L_WALL + " " * cat.TEXT_PADDING_SIDE + text[j]
                + " " * rightPadding + cat.R_WALL)
            for j in range(cat.TEXT_PADDING_VERTICAL):
                print(globalTextSpaces + cat.L_WALL + insideWidth * " " + cat.R_WALL)
        elif i == cat.OUTPUT_INDEX - 1:
            print(globalTextSpaces + cat.TL_CORNER_CHAR + cat.TOP * relativeCatPadding
            + cat.CAT[i] + cat.TOP * (insideWidth - cat.CAT_WIDTH - relativeCatPadding) + cat.TR_CORNER_CHAR)
        elif i == cat.OUTPUT_INDEX + 1:
            print(globalTextSpaces + cat.BL_CORNER_CHAR + cat.BOTTOM * relativeCatPadding
            + cat.CAT[i] + cat.BOTTOM * (insideWidth - cat.CAT_WIDTH - relativeCatPadding) + cat.BR_CORNER_CHAR)
        else:
            print(globalCatSpaces + cat.CAT[i])
    for i in range(cat.GLOBAL_PADDING):
        print()
main()
