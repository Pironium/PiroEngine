class MeshDeformer {
    constructor(mesh) {
        this.mesh = mesh;
        this.deformationMap = new Map();
    }

    applyDeformation(vertexIndex, deformationAmount) {
        if (!this.deformationMap.has(vertexIndex)) {
            this.deformationMap.set(vertexIndex, 0);
        }

        const currentDeformation = this.deformationMap.get(vertexIndex);
        const newDeformation = currentDeformation + deformationAmount;

        // Apply the deformation to the mesh's vertex position
        this.mesh.vertices[vertexIndex] += newDeformation;

        // Update the deformation map
        this.deformationMap.set(vertexIndex, newDeformation);
    }
}

class PiroEngine {
    // Existing engine code...

    enable3DMeshDeformation() {
        this.meshDeformer = new MeshDeformer(this.currentMesh);
    }

    deformMeshVertex(vertexIndex, deformationAmount) {
        if (this.meshDeformer) {
            this.meshDeformer.applyDeformation(vertexIndex, deformationAmount);
        } else {
            console.error("3D Mesh Deformation is not enabled. Call enable3DMeshDeformation() first.");
        }
    }
}

// Usage example:
const engine = new PiroEngine();
engine.loadMesh("example_model.obj");
engine.enable3DMeshDeformation();
engine.deformMeshVertex(0, 0.1); // Deform the first vertex
