# KeeGCPass

<!-- TOC -->
* [KeeGCPass](#keegcpass)
  * [Features](#features)
  * [Getting Started](#getting-started)
  * [Development Guidelines](#development-guidelines)
    * [GitFlow Workflow](#gitflow-workflow)
      * [Branching Model](#branching-model)
      * [Constraints](#constraints)
      * [Pros](#pros)
    * [Package Versioning](#package-versioning)
    * [Commit Message Types and Semantic Versioning](#commit-message-types-and-semantic-versioning)
  * [License](#license)
<!-- TOC -->

KeeGCPass is a command-line tool designed to simplify the management of secrets by seamlessly bridging the gap between
local KeePass files and Google Cloud Platform's Secret Manager. With KeeGCPass, you can effortlessly read, write, and
even copy secrets between GCP projects, all with a straightforward and intuitive CLI interface.

## Features

- Local KeePass Integration:
    - KeeGCPass allows you to access secrets stored in a local KeePass file with ease.
    - Simply provide the password via the CLI, and KeeGCPass will securely retrieve the necessary secrets.

- Google Cloud Platform Integration:
    - Seamlessly connect to GCP Secret Manager to store and manage your secrets in the cloud.
    - KeeGCPass can securely write secrets to GCP Secret Manager, ensuring they are protected and easily accessible when
      needed.

- Bidirectional Secret Management:
    - Not only can you read secrets from KeePass and write them to GCP Secret Manager, but you can also perform the
      reverse operation.
    - Retrieve secrets from GCP Secret Manager and store them securely in your KeePass file for local access.

- Cross-Project Secret Copying:
    - KeeGCPass makes it possible to copy secrets from one GCP project to another effortlessly.
    - This is particularly useful when you need to replicate configurations or share secrets between different projects.

- Terraform Integration:
    - Simplify your Terraform workflows by using KeeGCPass.
    - No longer do you need to manually set secret values via the GCP web UI.
    - KeeGCPass streamlines the process of managing secrets during infrastructure provisioning.

## Getting Started

To start using KeeGCPass, follow these simple steps:

1. **Installation**: Install KeeGCPass on your local machine by following the installation instructions in
   the [installation guide](INSTALL.md).

2. **Usage**: Refer to the [usage documentation](USAGE.md) for detailed instructions on how to use KeeGCPass for various
   operations, such as reading, writing, and copying secrets.

3. **Configuration**: Configure KeeGCPass with your GCP credentials and project settings to ensure a smooth integration
   with GCP Secret Manager. You can find instructions in the [configuration guide](CONFIGURATION.md).

4. **Examples**: Explore practical examples in the [examples directory](examples/) to see KeeGCPass in action, including
   common use cases and integration with Terraform.

## Development Guidelines

### GitFlow Workflow

KeeGCPass follows the GitFlow workflow for managing branches and releases. GitFlow is a popular branching model that
provides a clear structure for collaboration and release management in Git-based projects.

#### Branching Model

- **Unstable Branches**
    - Feature Branches:
        - These branches are used for developing new features.
        - They are short-lived and created based on the `dev`          branch.
    - Dev Branch:
        - The development branch where ongoing development and integration of features take place.

- **Stable Branches**
    - Release Branches:
        - These branches are created when preparing for a new release.
        - They are used to stabilize the code and perform release-specific tasks.
        - Release branches are based on the `dev` branch.
    - Hotfix Branches:
        - These branches are used to quickly address critical issues in production.
        - They are created from the `main` branch.
    - Main Branch:
        - The main branch represents the production-ready codebase.
        - It is always stable and reflects the latest production release.

- **Integration Branches**
    - Dev Branch:
        - The `dev` branch is the integration branch where feature branches are merged before being merged into
          the `main` branch.
    - Main Branch:
        - The `main` branch is the integration branch for release branches and hotfix branches.

#### Constraints

- **Always Merging**
    - In GitFlow, branches are always merged into other branches.
    - This helps maintain a structured flow of changes.

- **Branching Off**
    - Follow the rules for branching off from specific branches.
    - For example, feature branches should branch off from the `dev` branch.

- **Merging Into**
    - Branches must be merged into the appropriate target branches.
    - For example, feature branches are merged into the `dev` branch before eventually being merged into the `main`
      branch.

- **Branch Naming Conventions**
    - Adhere to naming conventions for branches to maintain consistency and clarity in the project.

- **Avoid Long-Running Feature Branches**
    - Long-running feature branches with extensive code changes can lead to significant merge conflicts within the team.
    - Consider breaking down features into smaller, manageable tasks to mitigate this issue.

#### Pros

- **Automation**
    - GitFlow operations can be automated using tools like "gitflow," making it easier to follow the workflow.

- **Well-Designed Workflow**
    - GitFlow provides a structured and well-designed workflow for managing development, releases, and hotfixes.

### Package Versioning

If you want to create a new package version:

```bash
cz bump
```

### Commit Message Types and Semantic Versioning

When following semantic versioning, the commit message types can be mapped to the version level they typically affect:

- __Major Version__ (`+1.0.0`):
    - None of the listed commit types are automatically associated with a major version change. Major version changes
      are typically decided based on more __significant project milestones__ or __breaking changes__.
        - example: `build(Poetry)!: change import path`

- __Minor Version__ (`0.+1.0`):
    - `feat:` Introducing a new feature is considered a minor version change.
        - example: `feat: add user authentication functionality`

- __Patch Version__ (`0.0.+1`):
    - `fix:` Fixing a bug corresponds to a patch version change.
        - example: `fix: resolve issue with data parsing`

- __Minor or Patch Version__ (Depends on Impact):
    - `build:` Changes to the build system or external dependencies can affect the minor or patch version, depending
      on the significance of the change.
        - Example: `build: Update dependency versions`
    - `ci:` Changes to CI configuration files and scripts may affect the minor or patch version, depending on their
      impact.
        - Example: `ci: Configure CI pipeline for automated testing`
    - `docs:` Documentation-only changes typically affect the minor or patch version, depending on their impact.
        - Example: `docs: Update installation instructions in README`
    - `perf:` Code changes aimed at improving performance can affect the minor or patch version, depending on their
      impact.
        - Example: `perf: Optimize database query`
    - `refactor:` Refactoring code may affect the minor or patch version, depending on its impact on the project.
        - Example: `refactor: Reorganize code for better readability`
    - `style:` Changes to code style that do not affect functionality can affect the minor or patch version, depending
      on their impact.
        - Example: `style: Format code for consistency`
    - `test:` Adding or correcting tests can affect the minor or patch version, depending on their impact on project
      stability.
        - Example: `test: Add unit tests for user authentication`

## License

KeeGCPass is open-source software licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it
as needed.

---

Simplify your secret management and streamline your cloud workflows with KeeGCPass. Get started today and take control
of your secrets!
