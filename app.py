"""
AI Trip Planner - Main Application
Integrates all modules: mood planning, budget optimization, conflict resolution, and Plan B generation
"""

from src.mood_planner import mood_based_travel_planner
from src.budget_optimizer import BudgetOptimizer
from src.conflict_resolver import ConflictResolver
from src.plan_b_generator import PlanBGenerator

class AITripPlanner:
    def __init__(self):
        self.trip_data = {}
        self.users = []
        self.itinerary = []
        
    def start_trip_planning(self, user_data):
        """Initialize trip planning with user information"""
        self.trip_data = user_data
        self.users = user_data.get('travelers', [])
        print(f"Trip planning started for {len(self.users)} travelers")
        
    def plan_by_mood(self, mood):
        """Get travel suggestions based on mood"""
        suggestions = mood_based_travel_planner(mood)
        return {
            'mood': mood,
            'suggestions': suggestions
        }
    
    def optimize_budget(self, total_budget, duration_days):
        """Optimize budget for the trip"""
        optimizer = BudgetOptimizer(total_budget, duration_days)
        allocation = optimizer.allocate_budget()
        return {
            'total_budget': total_budget,
            'daily_budget': total_budget / duration_days,
            'budget_allocation': allocation
        }
    
    def resolve_group_conflicts(self, preferences_dict):
        """Resolve conflicts among group members"""
        resolver = ConflictResolver()
        for member, prefs in preferences_dict.items():
            resolver.add_conflict(f"{member}: {prefs}")
        
        resolved = resolver.resolve_conflicts()
        return {
            'conflicts_identified': len(resolver.conflicts),
            'resolutions': resolved
        }
    
    def generate_backup_plans(self, original_plan):
        """Generate Plan B for various scenarios"""
        generator = PlanBGenerator(original_plan)
        backup_plans = generator.generate_all_backup_plans()
        return {
            'original_plan': original_plan,
            'backup_plans': backup_plans
        }
    
    def create_comprehensive_itinerary(self, destination, mood, budget, group_size):
        """Create a comprehensive trip itinerary"""
        itinerary = {
            'destination': destination,
            'mood_based_activities': self.plan_by_mood(mood),
            'budget_info': self.optimize_budget(budget, 7),  # 7-day trip
            'group_size': group_size,
            'backup_plans_available': True
        }
        self.itinerary = itinerary
        return itinerary
    
    def display_itinerary(self):
        """Display the complete itinerary"""
        if not self.itinerary:
            return "No itinerary created yet"
        
        print("\n" + "="*50)
        print("YOUR AI-POWERED TRIP ITINERARY")
        print("="*50)
        for key, value in self.itinerary.items():
            print(f"{key.upper()}: {value}")
        print("="*50 + "\n")
        
        return self.itinerary


# Example usage
if __name__ == "__main__":
    # Initialize the AI Trip Planner
    planner = AITripPlanner()
    
    # Start planning
    user_data = {
        'travelers': ['Alice', 'Bob', 'Charlie'],
        'duration_days': 7
    }
    planner.start_trip_planning(user_data)
    
    # Create itinerary
    itinerary = planner.create_comprehensive_itinerary(
        destination='Bali',
        mood='adventure',
        budget=3500,
        group_size=3
    )
    
    # Display results
    planner.display_itinerary()
    
    # Generate backup plans
    backup = planner.generate_backup_plans(itinerary)
    print("Backup Plans Generated:", backup['backup_plans'].keys())