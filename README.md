# crun-wasmtime-el
`crun` (and `conmon`) RPMs built with `wasmtime` support, for various Enterprise Linux distributions.

## Releases
For the latest release see https://github.com/justdan96/crun-wasmtime-el/releases.

## Creation
In this folder there are the scripts for generating the RPMs. There is a `justfile` for creating the RPMs for each version of EL (in this case AlmaLinux but should be compatible with any). There is also a `Dockerfile`, this Dockerfile creates the environment for building the RPM and then runs the commands to package the RPM. There is also an `alter-distro` script, that simply modifies the `%{dist}` RPM macro so each RPM is saved with the specific EL release they were built for.

## Credits
The original spec files for `crun` and `conmon` were taken from here and then updated: https://build.opensuse.org/project/show/devel:kubic:libcontainers:stable
