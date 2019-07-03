# Azathoth
Azathoth is LoveBite's API System.
The API System, written in Django and Python, is the link between the various end-user interfaces and the inner workings of LoveBite.

## Description

### What Azathoth isn't
Azathoth is not:
- A Blind Idiot God (at least not in this case)
- The Matching Algorithm
- The Push Notification System

### What Azathoth is responsible for
Azathoth acts as the middleware between the database, the matching algorithm, and the various end-user interfaces. In short, Azathoth needs to process every single call from the apps and output relevant information. It also has to deal with authentication.

## General Info

### Don't commit and drive.
LoveBite operate a "don't commit and drive" policy. Even if you have full read/write access to every single repo, always create a fork of the repo and then propose the changes. They will then be reviewed and, provided they do not break any features, they shall then be merged into the main repository. This is valid for all changes, even small bugfixes, as it ensures the integrity of the code that flows into production.

### We <3 Open Source.
LoveBite is open source, and we strive to keep it as open as possible. Whenever possible, choose open components in your changes over closed-source ones.


