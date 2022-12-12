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
        poetryOverrides = self: super: {
          dataconf = super.dataconf.overridePythonAttrs(old: {
            buildInputs = with super; [poetry];
          });
          sqlalchemy2-stubs = super.sqlalchemy2-stubs.overridePythonAttrs(old: {
            buildInputs = with super; [setuptools poetry];
          });
          async-scheduler-object = super.async-scheduler-object.overridePythonAttrs(old: {
            buildInputs = with super; [poetry];
          });
          hikari = super.hikari.overridePythonAttrs(old: {
            src = pkgs.fetchFromGitHub {   # TODO: https://github.com/hikari-py/hikari/issues/1399
              repo = "hikari";
              owner = "hikari-py";
              rev = old.version;
              hash = "sha256-vp3ujhXJEcaQnwC7Cn4Dn5FXGPTrEaHVC2S7GIfjno4=";
            };
            buildInputs = with super; [setuptools];
          });
        };
        app = pkgs.poetry2nix.mkPoetryApplication {
          projectDir = ./.;
          overrides = [pkgs.poetry2nix.defaultPoetryOverrides poetryOverrides];
        };
        packageName = "discord-top-role-bot";
      in {
        packages.${packageName} = app;
        defaultPackage = self.packages.${system}.${packageName};
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [poetry];
          inputsFrom = builtins.attrValues self.packages.${system};

          PIP_DISABLE_PIP_VERSION_CHECK="1";  # TODO: https://github.com/NixOS/nixpkgs/pull/198024
        };
      }
    );
}
