# Changelog

## [2027.0.0](https://github.com/aurumorinc/python-logging/compare/python-logging-v2026.2.0...python-logging-v2027.0.0) (2026-06-12)


### ⚠ BREAKING CHANGES

* The function get_windmill_context is renamed to get_windmill_traceparent and its return type has changed from a dictionary to an optional string.
* The minimum supported Python version is now 3.11.
* The minimum supported Python version is now 3.11.
* The environment field in LoggingSettings has been removed.

### Features

* add architectural and coding standards ([a158f01](https://github.com/aurumorinc/python-logging/commit/a158f010b9df5ae25fcfad3e4f28e243ea78e188))
* add architectural and coding standards ([0384a88](https://github.com/aurumorinc/python-logging/commit/0384a88d0d63df9b877dafe609ed1efce5aa1eb8))
* add logging environment configurations ([d166a0a](https://github.com/aurumorinc/python-logging/commit/d166a0a855b5f7471cb1fe367304f68912bfe2b1))
* add LoggingSettings configuration class ([b7b6627](https://github.com/aurumorinc/python-logging/commit/b7b6627673b0f56224189f104833f76eeb3d1eb8))
* add OpenTelemetry integration for logging ([5b12e0e](https://github.com/aurumorinc/python-logging/commit/5b12e0eccb8bfca976343e33f5c9dc780608a920))
* add windmill context extractor ([a437a5f](https://github.com/aurumorinc/python-logging/commit/a437a5f475e215633819d866dd82c92cd5a95651))
* expose integration modules in package init ([f2f883d](https://github.com/aurumorinc/python-logging/commit/f2f883dcdd7bd3ea9263d30b188a87cf864cbfdd))
* expose package modules in init file ([d182140](https://github.com/aurumorinc/python-logging/commit/d182140c30027c7f483c2963b484295c89bc5df9))
* implement automatic traceparent generation ([6eca7be](https://github.com/aurumorinc/python-logging/commit/6eca7be9f839ddcda67aa6962b24a25b8627a5e4))
* implement core logging configuration ([db012f9](https://github.com/aurumorinc/python-logging/commit/db012f92c791afadfb4fea0ce2a4f5850572c385))
* replace environment with stdout_format ([c65478e](https://github.com/aurumorinc/python-logging/commit/c65478e414d69ab270801eaa416ba7ed6d85f63a))
* upgrade minimum python version to 3.11 ([d397889](https://github.com/aurumorinc/python-logging/commit/d397889f89da2e84769ab242c5e1e3daccf64ada))


### Documentation

* add documentation to README ([3e672f5](https://github.com/aurumorinc/python-logging/commit/3e672f55df36f22682ed3b51d0c7891b8e1e273e))
* update documentation for logging integration ([da1d5ec](https://github.com/aurumorinc/python-logging/commit/da1d5ecc917f3ea3ee1214306833b50683d5ebd7))
* update documentation for logging integration ([05b5773](https://github.com/aurumorinc/python-logging/commit/05b5773af074d3f14c5a272394d8f2304dd14f16))
* update logging documentation and architecture ([8c03c85](https://github.com/aurumorinc/python-logging/commit/8c03c854658835014ea989fbf63b76b448540c94))
* update minimum python version requirement ([eef6bda](https://github.com/aurumorinc/python-logging/commit/eef6bdacc58d031191b39a8db4513d4cbe3050c3))


### Code Refactoring

* rename get_windmill_context to get_windmill_traceparent ([86aa6fb](https://github.com/aurumorinc/python-logging/commit/86aa6fb12742ffb9770bbd39bb1b2f72b0d747ae))


### Build System

* update python version to 3.11 ([db8c389](https://github.com/aurumorinc/python-logging/commit/db8c389e8d3e6877ee23ac52e513cd2907795ed1))
