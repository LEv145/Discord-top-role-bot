{
  description = "My Python application";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {self, nixpkgs, flake-utils}:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        app = pkgs.poetry2nix.mkPoetryApplication.projectDir = ./.;
        packageName = "lunohod-app";
      in {
        packages.${packageName} = app;
        defaultPackage = self.packages.${system}.${packageName};
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [(python310.withPackages (ps: with ps; [poetry]))];
          inputsFrom = builtins.attrValues self.packages.${system};
        };
      }
    );
}