import sys

# reverseコマンド
def reverse(inputPath, outputPath) -> str:
    # inputPathのファイルを読み込み、内容を逆にしたものをresultに格納
    result = ''
    with open(inputPath) as f:
        contents = f.read()
        result = contents[::-1]
    # resultを出力用ファイルに書き込み
    with open(outputPath, 'w') as f:
        f.write(result)
    
    return outputPath

# copyコマンド
def copy(inputPath, outputPath) -> str:
    with open(inputPath) as f:
        contents = f.read()
    with open(outputPath, 'w') as f:
        f.write(contents)
    
    return outputPath

# duplicate-contentsコマンド
def duplicate_contents(inputPath, n) -> str:
    with open(inputPath) as f:
        contents = f.read()
    with open(inputPath, 'w') as f:
        for i in range(int(n)):
            f.write(contents)
    
    return inputPath

# replace-stringコマンド
def replace_string(inputPath, replacedStr, newStr) -> str:
    newContent = ''
    with open(inputPath) as f:
        # ファイルの内容を読み込み、'needle' を 'newstring' に置き換えた新しい内容を作成
        for line in f:
            newContent += line.replace(replacedStr, newStr)
    with open(inputPath, 'w') as f:
        f.write(newContent)
    
    return inputPath

# コマンドの取得
command = sys.argv[1]
# print(command)

# reverse
if command == "reverse":
    # CLIの引数が正しく入力されているか確認
    if len(sys.argv) != 4:
        print("Usage: python <filePath> reverse <inputPath> <outputPath>")
    inputPath = sys.argv[2]
    outputPath = sys.argv[3]
    reverse(inputPath, outputPath)
    with open(outputPath) as f:
        print(f.read())
# copy
elif command == "copy":
    # CLIの引数が正しく入力されているか確認
    if len(sys.argv) != 4:
        print("Usage: python <filePath> copy <inputPath> <outputPath>")
    inputPath = sys.argv[2]
    outputPath = sys.argv[3]
    copy(inputPath, outputPath)
    with open(outputPath) as f:
        print(f.read())
# duplicate-contents
elif command == "duplicate-contents":
    # CLIの引数が正しく入力されているか確認
    if len(sys.argv) != 4:
        print("Usage: python <filePath> duplicate-contents <inputPath> n")
    inputPath = sys.argv[2]
    n = sys.argv[3]
    duplicate_contents(inputPath, n)
    with open(inputPath) as f:
        print(f.read())
# replace-string
elif command == "replace-string":
    if len(sys.argv) != 5:
        print("Usage: python <filePath> replace-string <inputPath> replaced-string newString")
    inputPath = sys.argv[2]
    replacedStr = sys.argv[3]
    newStr = sys.argv[4]
    replace_string(inputPath, replacedStr, newStr)
    with open(inputPath) as f:
        print(f.read())
# エラーハンドリング（入力されたコマンドが対象外だった場合）
else:
    print("Received an invalid command. Please enter the correct one and try again !")