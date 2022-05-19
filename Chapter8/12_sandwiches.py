def sandwich(*ingredients):
    """Print an arbitrary number of ingredients."""
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


sandwich('tuna')
sandwich('egg', 'bacon', 'mustard', 'chicken')
