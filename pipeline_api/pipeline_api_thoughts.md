# What this module will done?

Core purpose of this module is to handle all process in a thread safe pipeline but this module won't be generic QA or DevOps pipeline

API in the sentence can be deleted because i'm thinking aborting making this module as an API at beginning instead first purpose to write a local pipeline system that first checks quality controls, then have simulations with test cases and then deploys after all tests and quality checks done, it will securely  upload firmware to desired machine

## QualityChecks

I might change my idea and stop making Quality Control module an abstracted module, instead i can directly make it a module that checks requirements and flaws in circuits and other components that @Must be checked.

Secondly i want to turn experiment engine a direct module than an abstracted module that people or i must implement when i use everytime that's stupid design.

Workflow module is going to be abstracted because people might change it in a way they desire or work in local

