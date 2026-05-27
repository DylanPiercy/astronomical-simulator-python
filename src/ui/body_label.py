"""
Hover and pinned label UI for celestial bodies.
"""

from vpython import label, scene, vector

from physics.physics_diagnostics import PhysicsDiagnostics


class BodyLabel:
    """
    Displays hover labels and pinned labels for celestial bodies.
    """

    def __init__(self, bodies):
        self.bodies = bodies
        self.pinned_labels = {}
        self.hovered_body = None
        self.physics_diagnostics = PhysicsDiagnostics()

        self.hover_label = label(
            pos=vector(0, 0, 0),
            text="",
            visible=False,
            box=True,
            opacity=0.75,
            xoffset=20,
            yoffset=20,
            height=14,
        )

    def update(self) -> None:
        self._update_hover_label()
        self._update_pinned_labels()

    def handle_click(self) -> None:
        """
        Pins or unpins a label for the currently hovered body.
        """
        clicked_body = self.hovered_body

        if clicked_body is None:
            return

        if clicked_body in self.pinned_labels:
            self.pinned_labels[clicked_body].visible = False
            del self.pinned_labels[clicked_body]
            return

        self.pinned_labels[clicked_body] = label(
            pos=clicked_body.visual.pos,
            text=self._build_label_text(clicked_body),
            visible=True,
            box=True,
            opacity=0.75,
            xoffset=20,
            yoffset=20,
            height=14,
        )

    def _update_hover_label(self) -> None:
        self.hovered_body = self._get_body_from_object(scene.mouse.pick)

        if self.hovered_body is None or self.hovered_body in self.pinned_labels:
            self.hover_label.visible = False
            return

        self.hover_label.pos = self.hovered_body.visual.pos
        self.hover_label.text = self._build_label_text(self.hovered_body)
        self.hover_label.visible = True

    def _update_pinned_labels(self) -> None:
        for body, pinned_label in self.pinned_labels.items():
            pinned_label.pos = body.visual.pos
            pinned_label.text = self._build_label_text(body)

    def _get_body_from_object(self, picked_object):
        """
        Returns the celestial body matching the picked VPython object.
        """
        for body in self.bodies:
            if body.visual == picked_object:
                return body

        return None

    def _build_label_text(self, body) -> str:
        diagnostics = self.physics_diagnostics.calculate_body_snapshot(body)

        label_lines = [
            body.name,
            f"Type: {body.type.value}",
        ]

        if body.parent_body is not None:
            label_lines.extend(
                [
                    f"Parent: {body.parent_body.name}",
                    f"Distance from parent: {diagnostics.parent_distance:.3e} m",
                ]
            )

        label_lines.extend(
            [
                f"Speed: {diagnostics.speed:,.0f} m/s",
                f"Velocity: {self._format_vector(body.velocity)} m/s",
                f"Kinetic energy: {diagnostics.kinetic_energy:.3e} J",
                f"Momentum: {diagnostics.linear_momentum_magnitude:.3e} kg m/s",
                f"Mass: {body.mass:.3e} kg",
                f"Radius: {body.radius:,.0f} m",
            ]
        )

        return "\n".join(label_lines)

    def _format_vector(self, value: vector) -> str:
        """
        Formats a VPython vector for display.
        """
        return f"({value.x:.3e}, {value.y:.3e}, {value.z:.3e})"
