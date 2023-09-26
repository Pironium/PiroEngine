using System;
using System.Collections.Generic;

namespace PiroEngine
{
    public class MultiPlatformCompiler
    {
        private List<string> supportedPlatforms = new List<string>
        {
            "Windows",
            "Android",
            "iPhone",
            "macOS",
            "Linux",
            "PS4",
            "Xbox One"
        };

        public void CompileGameForAllPlatforms(string gameName)
        {
            Console.WriteLine($"Compiling {gameName} for multiple platforms:");

            foreach (string platform in supportedPlatforms)
            {
                string compiledGame = CompileGame(gameName, platform);
                Console.WriteLine($"- {gameName} compiled for {platform}: {compiledGame}");
            }

            Console.WriteLine($"Compilation complete for {gameName}.");
        }

        private string CompileGame(string gameName, string platform)
        {
            string compiledGame = "";

            switch (platform)
            {
                case "Windows":
                    compiledGame = CompileForWindows(gameName);
                    break;
                case "Android":
                    compiledGame = CompileForAndroid(gameName);
                    break;
                case "iPhone":
                    compiledGame = CompileForiPhone(gameName);
                    break;
                case "macOS":
                    compiledGame = CompileForMacOS(gameName);
                    break;
                case "Linux":
                    compiledGame = CompileForLinux(gameName);
                    break;
                case "PS4":
                    compiledGame = CompileForPS4(gameName);
                    break;
                case "Xbox One":
                    compiledGame = CompileForXboxOne(gameName);
                    break;
                default:
                    compiledGame = "Platform not supported.";
                    break;
            }

            return compiledGame;
        }

        private string CompileForWindows(string gameName)
        {
            // Code to compile the game for Windows
            return $"Windows version of {gameName} compiled successfully.";
        }

        private string CompileForAndroid(string gameName)
        {
            // Code to compile the game for Android
            return $"Android version of {gameName} compiled successfully.";
        }

        private string CompileForiPhone(string gameName)
        {
            // Code to compile the game for iPhone
            return $"iPhone version of {gameName} compiled successfully.";
        }

        private string CompileForMacOS(string gameName)
        {
            // Code to compile the game for macOS
            return $"macOS version of {gameName} compiled successfully.";
        }

        private string CompileForLinux(string gameName)
        {
            // Code to compile the game for Linux
            return $"Linux version of {gameName} compiled successfully.";
        }

        private string CompileForPS4(string gameName)
        {
            // Code to compile the game for PS4
            return $"PS4 version of {gameName} compiled successfully.";
        }

        private string CompileForXboxOne(string gameName)
        {
            // Code to compile the game for Xbox One
            return $"Xbox One version of {gameName} compiled successfully.";
        }
    }
}
