extends Control

@export var play_tab_button: Button
@export var play_tab: Panel
@export var loadout_tab: Panel
@export var drip_tab: Panel
@export var career_tab: Panel
@export var store_tab: Panel

func _ready():
	play_tab_button.set_pressed(true)

func _on_play_tab_pressed():
	switch_tab("play_tab")
	
func _on_loadout_tab_pressed():
	switch_tab("loadout_tab")
	
func switch_tab(tab: String) -> void:
	play_tab.visible = false
	loadout_tab.visible = false
	drip_tab.visible = false
	career_tab.visible = false
	store_tab.visible = false
	
	if tab == "play_tab":
		play_tab.visible = true
	elif tab == "loadout_tab":
		loadout_tab.visible = true
	elif tab == "drip_tab":
		drip_tab.visible = true
	elif tab == "career_tab":
		career_tab.visible = true
	elif tab == "store_tab":
		store_tab.visible = true
		
