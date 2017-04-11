SublimeLinter-contrib-nvcc
================================

[![Build Status](https://travis-ci.org/blahgeek/SublimeLinter-contrib-nvcc.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-nvcc)

This linter plugin for [SublimeLinter][docs] provides an interface to [nvcc](http://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/). It will be used with files that have the “cuda-c++/cuda-c/cuda” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that CUDA Toolkit is installed on your system.

Also, you must install [CUDA C++](https://github.com/harrism/sublimetext-cuda-cpp) plugin to make sublimetext detect CUDA syntax.

**Note:** This plugin has only been tested on CUDA 8.0. Contributes and feedbacks are welcome.

### Linter configuration
In order for `nvcc` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `nvcc`, you can proceed to install the SublimeLinter-contrib-nvcc plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `nvcc`. Among the entries you should see `SublimeLinter-contrib-nvcc`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

In addition to the standard SublimeLinter settings, SublimeLinter-contrib-nvcc provides its own settings.

|Setting|Description|
|:------|:----------|
|include_dirs|A list of directories to be added to the header search paths (-I is not needed).|
|extra_flags|A string with extra flags to pass to nvcc. These should be used carefully, as they may cause linting to fail.|

In project-specific settings, `$project_folder` or `${project_folder}` can be used to specify relative path.

    "SublimeLinter":
    {
        "linters":
        {
            "nvcc": {
                "extra_flags": "-I${project_folder}/foo",
                "include_dirs": [
                    "${project_folder}/3rdparty/bar/include",
                    "${project_folder}/3rdparty/baz"
                ]
            }
        }
    },


## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
