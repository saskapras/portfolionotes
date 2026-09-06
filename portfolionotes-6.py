# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: PortfolioNotes
def delete_item(item_id: str, confirm: bool = False, items: dict = None) -> dict:
    if items is None:
        items = {}
    if item_id not in items:
        return {"success": False, "message": f"No item with id '{item_id}' found."}
    if not confirm:
        return {"success": False, "message": "A confirmation flag (confirm=True) is required to delete an item."}
    del items[item_id]
    return {"success": True, "message": f"Item '{item_id}' deleted successfully."}
