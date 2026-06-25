# Changelog v2.0.0

## Breaking Changes

* **Renaming of Windmill Configuration Fields**
  Windmill configuration fields have been updated to use full naming conventions instead of abbreviations to improve clarity and consistency. This change will cause existing configurations to fail if not updated.
  * **Migration:** Identify all abbreviated configuration keys in your configuration files or environment variables and update them to the new full-name equivalents as defined in the updated documentation.
  * **Commits:** [1ed4b43](https://github.com/aurumorinc/lume-python/commit/1ed4b438), [a4bb86d](https://github.com/aurumorinc/lume-python/commit/a4bb86da)
