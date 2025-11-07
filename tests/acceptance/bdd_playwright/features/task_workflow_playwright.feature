Feature: Task Tracker Manual Workflow with Playwright (US033)
  As a user of the task tracker application
  I want to create, complete, and view tasks through the web interface
  So that I can manage my tasks effectively using Playwright automation

  Background:
    Given the task tracker application is running
    And I am using a web browser

  Scenario: Complete task workflow with Playwright - Create, Complete, and View Report
    Given I am on the home page
    When I click "Add Task" in the navigation menu
    Then I should be on the task creation page
    When I fill out the task form with:
      | Field       | Value                           |
      | Title       | Playwright BDD Integration Task |
      | Description | Created using Playwright BDD   |
    And I submit the task form
    Then I should be redirected to the task list page
    And I should see "Playwright BDD Integration Task" in the task list
    When I click "Mark Complete" on the "Playwright BDD Integration Task"
    Then the task should be marked as completed
    And I should see the task status updated
    When I click "Report" in the navigation menu
    Then I should be on the task report page
    And I should see "Playwright BDD Integration Task" in the task summary
    And I should see the completion status in the report

  Scenario: Simple task creation workflow with Playwright
    Given I am on the task creation page
    When I enter "Quick Playwright BDD Task" as the title
    And I enter "Testing Playwright BDD functionality" as the description
    And I submit the form
    Then I should see "Quick Playwright BDD Task" on the task list page

  Scenario: Task creation and verification workflow with Playwright
    Given I open the task management page
    When I add a new task with title "Playwright Verification Task"
    Then I should see "Playwright Verification Task" in the task list
    And I should be able to view it in the task report