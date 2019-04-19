### Generating an updated UML diagram

1. Navigate to the octa directory (`cd ~/octa` if you're on Zara's computer).
2. Run `workon octa` inside 1.
3. Run: `python manage.py graph_models -a -o octa_uml.png`

### Branching Strategy
1. `octa-develop`: This is the branch used for regular development and isn't tied to any release in particular.
2. `octa-qa`: This is the branch used for wider user acceptance testing. `octa-develop` should be periodically merged into `octa-qa` if we're doing a release or a piece of functionality has been completely.
3. `master`: This is the production branch. Once we're satisfied with the results of UAT on the `octa-qa` branch, we should `tag` the latest commit and then merge `octa-qa` -> `master`
4. feature branches: Everytime we want to implement some new functionality, we should cut a new feature branch off of `octa-develop` and then submit pull requests for review. Once it's been approved, we can merge it into `octa-develop` and delete the feature branch. We should delete these post merge to prevent too many of these from lying around in our repository.
