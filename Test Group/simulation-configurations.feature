
Feature: simulation configurations

Scenario: Validate that Adding  Stochastic HITS driver profiles with valid target speed is successful

    Given I open traffic UI
     When I enter valid input values for target speed and click add profile
     Then I should see driver profile being added and visible in driver profile table

Scenario: Validate that Adding  Stochastic HITS driver profiles with valid Beta value is successful

    Given I open traffic UI
     When I enter valid input values for beta and click add profile
     Then I should see driver profile being added and visible in driver profile table

Scenario: Validate that Adding  Stochastic HITS driver profiles with valid Alpha value is successful

    Given I open traffic UI
     When I enter valid input values for alpha and click add profile
     Then I should see driver profile being added and visible in driver profile table

Scenario: Validate that adding Stochastic HITS driver with invalid target speed throws an error

    Given I open traffic UI
     When I enter invalid input values for target speed and click add profile
     Then I should see driver profile not being added and an error is shown

Scenario: Validate that adding Stochastic HITS driver with invalid beta throws an error

    Given I open traffic UI
     When I enter invalid input values for beta and click add profile
     Then I should see driver profile not being added and an error is shown

Scenario: Validate that adding Stochastic HITS driver with invalid alpha throws an error

    Given I open traffic UI
     When I enter invalid input values for alpha and click add profile
     Then I should see driver profile not being added and an error is shown

Scenario: Validate the error message is displayed under input field for invalid target speed
    Given I open traffic UI
     When I enter invalid input values for target speed and click add profile
     Then I should see driver profile not being added and an error is shown

Scenario: Validate the error message is displayed under input field for invalid alpha value

    Given I open traffic UI
     When I enter invalid input values for beta and click add profile
     Then I should see driver profile not being added and an error is shown

Scenario: Validate the error message is displayed under input field for invalid beta value

    Given I open traffic UI
     When I enter invalid input values for alpha and click add profile
     Then I should see driver profile not being added and an error is shown

Scenario: Validate that Adding  Stochastic HITS plus AI driver profiles with valid target speed is successful

    Given I open traffic UI
     When I select any AI model radio button, enter target speed and click add profile
     Then I should see the driver profile being added and visible in the driver profile table

Scenario: Validate that Adding Stochastic HITS plus AI driver profiles with invalid target speed is not successful

    Given I open traffic UI
     When I select any AI model radio button, enter invalid target speed and click add profile
     Then I should see the driver profile NOT added and is NOT visible in the driver profile table

Scenario: Validate the presence of Stochastic HITS plus AI driver

    Given I open traffic UI
     When I goto vehicle and driver profiles under traffic configuration
     Then I should see Vehicle Profiles, Rule-Based Driver Profiles & AI Driver Profiles configuration input fields appear
     Then I should see an error for value greater than zero