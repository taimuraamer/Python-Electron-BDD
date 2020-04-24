
Feature: Configurations

Scenario: Verify correct configurations are loaded

    Given I open traffic UI
     When I select the project folder and click start
     Then I should see configurations being imported correctly

Scenario: Verify incorrect configurations are loaded
    Given I open traffic UI
     When I select the project folder and clear the field
     When I click start configurations
     Then I should see configurations error and path not selected

