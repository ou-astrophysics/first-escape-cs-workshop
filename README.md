# The First ESCAPE Citizen Science Workshop
This repository contains material and resources for the first ESCAPE Citizen Science workshop.

## Workshop Website
You can find details of the workshop's sessions and download the slides for contributed talks and tutorials from the [workshop website](https://indico.in2p3.fr/event/21939/).

## Tutorial Code and Data
Each of the subfolders in this repository contains the Python code and various data that were used in each of the workshop's tutorials.

* `project_builder_introduction` - Contains the datasets used for the ["Building a _Zooniverse_ Project"](https://indico.in2p3.fr/event/21939/contributions/89045/) tutorial on the _Zooniverse_ Project Builder from the first day of the workshop.
* `advanced_project_building` - Contains the Jupyter notebook	(Python code and comments) and datasets used for the ["Advanced Project Building](https://indico.in2p3.fr/event/21939/contributions/89046/) tutorial from the second day of the workshop.
* `aggregation_tutorial` - Contains the Jupyter notebook (Python code and comments) and datasets used for the ["Advanced Caesar Usage](https://indico.in2p3.fr/event/21939/contributions/89053/) tutorial by Dr Coleman Krawczyk. This tutorial from the second day of the workshop focussed on the `panoptes_aggregation` utility.
* `integrating_machine_learning` - Contains the Jupyter notebook (Python code and comments) and datasets used for the ["Citizen Science with Machine Learning"](https://indico.in2p3.fr/event/21939/contributions/89065/) tutorial from day 2 of the workshop.

## Workshop Recordings
All presentations and tutorials from the first two days of the workshop were recorded and will soon be posted online. **Links will be posted here when they are available.**

## Links, Additional Help and Resources
During the workshop, we mentioned several additional resources that you may find very useful when building your own citizen science project using the _Zooniverse_ Project Builder. We've compiled a list for your convenience.

* [The Main _Zooniverse_ Website](http://zooniverse.org) - The starting point for researchers interested in Citizen Science. Create a **free** _Zooniverse_ account, browse other projects for inspiration, contribute yourself as a citizen scientist, and build your own project.
* [The _Caesar_ Web User Interface](https://caesar.zooniverse.org) - An online interface for the _Caesar_ advanced retirement and aggregation engine. See the ["Introducing Caesar"](https://indico.in2p3.fr/event/21939/contributions/89043/) presentation and the [workshop tutorials](https://indico.in2p3.fr/event/21939/timetable/#20201203), for tips and advice on how to use Caesar to supercharge your _Zooniverse_ project.
* [Zooniverse project builder help pages](https://help.zooniverse.org) - A great resource with practical guidance, tips and advice for building great Citizen Science projects.
* [The `panoptes_client` documentation](https://panoptes-python-client.readthedocs.io/en/v1.1/) - A comprehensive reference for the Panoptes Python Client that was used extensively in the ["Advanced Project Building](https://indico.in2p3.fr/event/21939/contributions/89046/) and ["Citizen Science with Machine Learning"](https://indico.in2p3.fr/event/21939/contributions/89065/) tutorials.
* [The `panoptes_aggregation` documentation](https://aggregation-caesar.zooniverse.org/docs) - A comprehensive reference for the Panoptes Aggregation tool that was explained in the ["Advanced Caesar Usage](https://indico.in2p3.fr/event/21939/contributions/89053/) tutorial.
* [Amazon Web Services (AWS)](https://aws.amazon.com) - A cloud computation provider that will let you create you own SQS queue like the one that was used in the ["Citizen Science with Machine Learning"](https://indico.in2p3.fr/event/21939/contributions/89065/) tutorial. You can register for a free account and **some** services are available free of charge **up to specific usage limits**. Be careful you don't exceed these limits or you may end up with a bill to pay!
* [AWS Simple Queue Service (SQS)](https://aws.amazon.com/sqs/) - Information about the SQS message queueing system that can be used together with Caesar to implement computationally intensive extraction and reduction tasks and apply them to your project's classifications.
