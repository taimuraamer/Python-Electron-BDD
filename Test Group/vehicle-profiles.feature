
Feature: vehicle profiles

Scenario: Validate adding vehicle profiles for valid physical property value of  Maximum Speed

    Given I open traffic UI
     When I enter valid input values for physical property of maximum speed and click add profile
     Then I should see vehicle profile being added and visible in profile table

Scenario: Validate adding vehicle profiles for valid physical property value of Brake maximum deceleration

    Given I open traffic UI
     When I enter valid input values for physical property of brake maximum deceleration and click add profile
     Then I should see vehicle profile being added and visible in profile table

Scenario: Validate adding vehicle profiles for valid physical property value of height

    Given I open traffic UI
     When I enter valid input values for physical property of height and click add profile
     Then I should see vehicle profile being added and visible in profile table

Scenario: Validate adding vehicle profiles for valid physical property value of cdA

    Given I open traffic UI
     When I enter valid input values for physical property of cdA and click add profile
     Then I should see vehicle profile being added and visible in profile table

Scenario: Validate adding vehicle profiles for valid physical property value of width

    Given I open traffic UI
     When I enter valid input values for physical property of width and click add profile
     Then I should see vehicle profile being added and visible in profile table

Scenario: Validate adding vehicle profiles for valid physical property value of engine maximum acceleration

    Given I open traffic UI
     When I enter valid input values for physical property of engine maximum acceleration and click add profile
     Then I should see vehicle profile being added and visible in profile table

Scenario: Validate adding vehicle profiles for valid physical property value of Mass

    Given I open traffic UI
     When I enter valid input values for physical property of mass and click add profile
     Then I should see vehicle profile being added and visible in profile table

Scenario: Validate adding vehicle profiles for valid physical property value of length

    Given I open traffic UI
     When I enter valid input values for physical property of length and click add profile
     Then I should see vehicle profile being added and visible in profile table

Scenario: Validate adding vehicle profile's physical property empty value of Maximum Speed throws an error

    Given I open traffic UI
     When I enter empty input values for physical property of maximum speed and click add profile
     Then I should see an error being shown and vehicle profile not being added

Scenario: Validate adding vehicle profile's physical property empty value of Brake Maximum Deceleration throws an error

    Given I open traffic UI
     When I enter empty input values for physical property of brake maximum deceleration speed and click add profile
     Then I should see an error being shown and vehicle profile not being added

Scenario: Validate adding vehicle profile's physical property empty value of height throws an error

    Given I open traffic UI
     When I enter empty input values for physical property of height and click add profile
     Then I should see an error being shown and vehicle profile not being added

Scenario: Validate adding vehicle profile's physical property empty value of cdA throws an error

    Given I open traffic UI
     When I enter empty input values for physical property of cdA and click add profile
     Then I should see an error being shown and vehicle profile not being added

Scenario: Validate adding vehicle profile's physical property empty value of width throws an error

    Given I open traffic UI
     When I enter empty input values for physical property of width and click add profile
     Then I should see an error being shown and vehicle profile not being added

Scenario: Validate adding vehicle profile's physical property empty value of Engine Max. Acceleration throws an error

    Given I open traffic UI
     When I enter empty input values for physical property of engine max. acceleration and click add profile
     Then I should see an error being shown and vehicle profile not being added

Scenario: Validate adding vehicle profile's physical property empty value of mass throws an error

    Given I open traffic UI
     When I enter empty input values for physical property of mass and click add profile
     Then I should see an error being shown and vehicle profile not being added

Scenario: Validate adding vehicle profile's physical property empty value of length throws an error

    Given I open traffic UI
     When I enter empty input values for physical property of length and click add profile
     Then I should see an error being shown and vehicle profile not being added

Scenario: Validate adding vehicle profiles for invalid physical property of Maximum Speed throws an error

    Given I open traffic UI
     When I enter invalid input values for physical property of maximum speed and click add profile
     Then I should see an error for value greater than or equals to 90

Scenario: Validate adding vehicle profiles for invalid physical property of brake maximum deceleration throws an error

    Given I open traffic UI
     When I enter invalid input values for physical property of break maximum deceleration and click add profile
     Then I should see an error for value less than zero

Scenario: Validate adding vehicle profiles for invalid physical property of height throws an error

    Given I open traffic UI
     When I enter invalid input values for physical property of height and click add profile
     Then I should see an error for value greater than zero

Scenario: Validate adding vehicle profiles for invalid physical property of cdA throws an error

    Given I open traffic UI
     When I enter invalid input values for physical property of cdA and click add profile
     Then I should see an error for value greater than zero

Scenario: Validate adding vehicle profiles for invalid physical property of width throws an error

    Given I open traffic UI
     When I enter invalid input values for physical property of width and click add profile
     Then I should see an error for value greater than zero

Scenario: Validate adding vehicle profiles for invalid physical property of Engine Maximum acceleration throws an error

    Given I open traffic UI
     When I enter invalid input values for physical property of engine maximum acceleration and click add profile
     Then I should see an error for value greater than zero

Scenario: Validate adding vehicle profiles for invalid physical property of Mass throws an error

    Given I open traffic UI
     When I enter invalid input values for physical property of mass and click add profile
     Then I should see an error for value greater than zero

Scenario: Validate adding vehicle profiles for invalid physical property of length throws an error

    Given I open traffic UI
     When I enter invalid input values for physical property of length and click add profile
     Then I should see an error for value greater than zero