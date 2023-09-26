// Fire Shader Code
// This shader creates a realistic fire effect

float4 FireShader(PixelInput input) : SV_TARGET
{
    float4 color = float4(1.0f, 0.5f + sin(input.uv.x * input.uv.y * 10 + _Time.y) * 0.5f, 0.0f, 1.0f);
    return color;
}
