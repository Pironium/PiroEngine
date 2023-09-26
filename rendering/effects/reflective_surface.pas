unit ReflectiveSurface;

interface

uses
  SysUtils, Graphics;

type
  TReflectiveSurface = class
  private
    FWidth, FHeight: Integer;
    FSurfaceData: array of array of TColor;
  public
    constructor Create(Width, Height: Integer);
    procedure RenderReflection(SourceImage: TBitmap);
    procedure ApplyReflectionEffect(DestinationImage: TBitmap);
  end;

implementation

constructor TReflectiveSurface.Create(Width, Height: Integer);
begin
  FWidth := Width;
  FHeight := Height;
  SetLength(FSurfaceData, FWidth, FHeight);
end;

procedure TReflectiveSurface.RenderReflection(SourceImage: TBitmap);
var
  X, Y: Integer;
begin
  for X := 0 to FWidth - 1 do
    for Y := 0 to FHeight - 1 do
    begin
      // Определение цвета пикселя из исходного изображения и его отражения
      FSurfaceData[X, Y] := SourceImage.Canvas.Pixels[X, FHeight - Y - 1];
    end;
end;

procedure TReflectiveSurface.ApplyReflectionEffect(DestinationImage: TBitmap);
var
  X, Y: Integer;
begin
  for X := 0 to FWidth - 1 do
    for Y := 0 to FHeight - 1 do
    begin
      // Применение отражения к изображению
      DestinationImage.Canvas.Pixels[X, Y] := FSurfaceData[X, Y];
    end;
end;

end.
