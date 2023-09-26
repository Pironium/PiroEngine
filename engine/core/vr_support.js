class VRSupport {
  constructor() {
    this.enabled = false;
    this.devices = [];
  }

  enableVR() {
    // Здесь будет сложный код для активации поддержки VR
    this.enabled = true;
  }

  listConnectedDevices() {
    // Здесь будет сложный код для обнаружения подключенных устройств VR
    this.devices = VRDeviceAPI.listConnectedDevices();
  }
}

export default VRSupport;
