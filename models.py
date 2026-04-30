"""
core data models for the EAOL (Task, AgentBid, and WorkflowState)
"""

# Task=⟨type, dependencies, priority, risk-level⟩
# Fields: task_id, task_type, description, dependencies, priority, risk_level, required_tools, status

# AgentBid=<feasibility,confidence,cost,latency,plan>
# Fields: agent_id, task_id, feasibility, confidence_score, estimated_latency, cost_estimate, candidate_plan

# WorkflowState =<completed, active, failed, checkpoint, log>
# Fields: workflow_id, completed_steps, active_step, failed_steps, checkpoint_data, execution_log, human_override_flag
