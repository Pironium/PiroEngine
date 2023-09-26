import Foundation

public class PiroScriptInteractiveDebugger {
    private var breakpoints: [String: [Int]] = [:]
    private var currentLine = 0

    public init() {}

    public func setBreakpoint(file: String, line: Int) {
        if breakpoints[file] == nil {
            breakpoints[file] = []
        }
        breakpoints[file]?.append(line)
    }

    public func runScript(script: String) {
        let scriptLines = script.components(separatedBy: "\n")
        while currentLine < scriptLines.count {
            let currentFile = "ScriptFile.pis" // Здесь может быть реализована поддержка множества файлов
            if let linesWithBreakpoints = breakpoints[currentFile] {
                if linesWithBreakpoints.contains(currentLine) {
                    print("Breakpoint hit at line \(currentLine + 1) in \(currentFile)")
                    // Здесь можно добавить дополнительные функции для отладки, например, просмотр значений переменных.
                    return
                }
            }
            // Здесь можно добавить интерпретацию кода 'PiroScript' и его выполнение.
            // Для примера, мы просто будем симулировать выполнение одной строки кода за итерацию.
            print("Executing line \(currentLine + 1): \(scriptLines[currentLine])")
            currentLine += 1
        }
        print("Script execution completed.")
    }
}
