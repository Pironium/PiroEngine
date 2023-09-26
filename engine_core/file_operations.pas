unit file_operations;

interface

uses
  SysUtils;

type
  TFileOperations = class
    class function ReadBytes(const FileName: string; var Buffer: TArray<Byte>): Boolean;
    class function WriteBytes(const FileName: string; const Buffer: TArray<Byte>): Boolean;
  end;

implementation

class function TFileOperations.ReadBytes(const FileName: string; var Buffer: TArray<Byte>): Boolean;
var
  FileStream: TFileStream;
begin
  Result := False;
  try
    FileStream := TFileStream.Create(FileName, fmOpenRead);
    try
      SetLength(Buffer, FileStream.Size);
      FileStream.ReadBuffer(Buffer[0], Length(Buffer));
      Result := True;
    finally
      FileStream.Free;
    end;
  except
    on E: Exception do
      Writeln('Error reading file: ', E.Message);
  end;
end;

class function TFileOperations.WriteBytes(const FileName: string; const Buffer: TArray<Byte>): Boolean;
var
  FileStream: TFileStream;
begin
  Result := False;
  try
    FileStream := TFileStream.Create(FileName, fmCreate);
    try
      FileStream.WriteBuffer(Buffer[0], Length(Buffer));
      Result := True;
    finally
      FileStream.Free;
    end;
  except
    on E: Exception do
      Writeln('Error writing file: ', E.Message);
  end;
end;

end.
