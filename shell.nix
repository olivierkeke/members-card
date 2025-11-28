# shell.nix
let
  # We pin to a specific nixpkgs commit for reproducibility.
  # Last updated: 2024-04-29. Check for new commits at https://status.nixos.org.
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-25.05") {};
in pkgs.mkShell {
  packages = [
    pkgs.gimp
    pkgs.inkscape
    # pkgs.openblas
    # pkgs.stdenv
    # pkgs.libz
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      # select Python packages here
      pip
    ]))
  ];
  LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib";
}
