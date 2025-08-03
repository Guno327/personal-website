{pkgs ? import <nixpkgs> {}}: let
  inherit (pkgs) lib stdenv;
in
  pkgs.mkShell {
    shellHook = ''
      export C_INCLUDE_PATH=$(pwd)/hdr
    '';

    NIX_LD_LIBRARY_PATH =
      lib.makeLibraryPath [
      ];
    NIX_LD = lib.fileContents "${stdenv.cc}/nix-support/dynamic-linker";

    packages = with pkgs; [
      go
      typescript
    ];
  }
