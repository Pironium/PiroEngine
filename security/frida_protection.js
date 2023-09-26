// PiroEngine Frida Protection Module
// Copyright (c) 2023 Pironium Inc.

const { Memory, NativeFunction } = require('frida');

const engineBaseAddress = Module.findBaseAddress('PiroEngine');

if (engineBaseAddress) {
  // Define our custom function to protect against Frida injection
  const protectAgainstFrida = new NativeFunction(
    engineBaseAddress.add(0x1A2B3C4D), // Replace with the actual address
    'int',
    ['pointer', 'pointer'],
    {
      abi: 'default',
    }
  );

  // Memory protection against Frida
  Memory.protect(protectAgainstFrida, Process.pageSize, 'rwx');

  // Implementing anti-Frida detection
  const checkFrida = () => {
    if (Process.isDebuggerAttached()) {
      console.log('Debugger Detected! Exiting...');
      Process.exit();
    }
    // Additional anti-Frida checks can be added here
  };

  // Execute anti-Frida checks periodically
  setInterval(checkFrida, 5000); // Check every 5 seconds
} else {
  console.error('PiroEngine base address not found. Frida protection not applied.');
}
