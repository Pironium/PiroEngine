// ShaderEffects class for creating custom texture effects
class ShaderEffects {
  constructor() {
    this.shaderProgram = null;
    this.canvas = null;
    this.gl = null;
  }

  // Initialize the shader program and WebGL context
  init(canvasId) {
    this.canvas = document.getElementById(canvasId);
    this.gl = this.canvas.getContext("webgl");

    if (!this.gl) {
      console.error("WebGL is not supported in this browser.");
      return;
    }

    // Vertex shader code
    const vsSource = `
      attribute vec4 aVertexPosition;
      attribute vec2 aTextureCoord;
      varying highp vec2 vTextureCoord;
      void main(void) {
        gl_Position = aVertexPosition;
        vTextureCoord = aTextureCoord;
      }
    `;

    // Fragment shader code (customizable by developers)
    const fsSource = `
      varying highp vec2 vTextureCoord;
      uniform sampler2D uSampler;
      void main(void) {
        highp vec4 texelColor = texture2D(uSampler, vTextureCoord);
        // Apply custom shader effects here (e.g., tint, blur, distort)
        gl_FragColor = texelColor;
      }
    `;

    // Compile and link the shaders
    this.shaderProgram = this.initShaderProgram(this.gl, vsSource, fsSource);
    if (!this.shaderProgram) {
      console.error("Unable to initialize the shader program.");
      return;
    }

    this.gl.useProgram(this.shaderProgram);
  }

  // Create and compile a shader program
  initShaderProgram(gl, vsSource, fsSource) {
    const vertexShader = this.loadShader(gl, gl.VERTEX_SHADER, vsSource);
    const fragmentShader = this.loadShader(gl, gl.FRAGMENT_SHADER, fsSource);

    const shaderProgram = gl.createProgram();
    gl.attachShader(shaderProgram, vertexShader);
    gl.attachShader(shaderProgram, fragmentShader);
    gl.linkProgram(shaderProgram);

    if (!gl.getProgramParameter(shaderProgram, gl.LINK_STATUS)) {
      console.error("Unable to initialize the shader program: " + gl.getProgramInfoLog(shaderProgram));
      return null;
    }

    return shaderProgram;
  }

  // Create and compile a shader
  loadShader(gl, type, source) {
    const shader = gl.createShader(type);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);

    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
      console.error("An error occurred compiling the shaders: " + gl.getShaderInfoLog(shader));
      gl.deleteShader(shader);
      return null;
    }

    return shader;
  }
}
