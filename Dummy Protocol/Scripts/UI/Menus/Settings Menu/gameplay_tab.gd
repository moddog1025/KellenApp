extends PanelContainer

@export var v_sens_slider: HSlider
@export var v_sens_input: LineEdit

var default_v_sens: float = 0.5

func _ready():
	v_sens_slider.value = default_v_sens
	v_sens_input.text = str(default_v_sens)

func _on_vert_sens_slider_value_changed(value):
	v_sens_input.text = str(value)
	
func _on_vert_sens_input_biox_text_submitted(new_text):
	v_sens_slider.value = 0.1
	v_sens_input.text = new_text
	#if new_text != "" and new_text.to_float() != null:
		#v_sens_slider.value = float(new_text)
		#v_sens_input.text = str(new_text)


func _on_vert_sens_input_box_text_changed(new_text):
	v_sens_slider.value = 0.1
	v_sens_input.text = new_text
