import torch

def autoregressive_prediction(rave_model, fedformer_model, initial_context, num_steps):
    # Initialize a sequence to store the generated audio samples
    generated_sequence = initial_context

    # Set the models to evaluation mode
    rave_model.eval()
    fedformer_model.eval()

    with torch.no_grad():
        # Convert the initial context to a tensor 
        initial_context_tensor = torch.from_numpy(initial_context).to(rave_model.device)

        for step in range(num_steps):
            # Use the RAVE model to generate an initial prediction
            next_sample_rave = rave_model.generate_sample(initial_context_tensor)

            # Use the FEDformer model to refine the prediction
            next_sample_fedformer = fedformer_model.refine_sample(next_sample_rave)

            # Convert the refined sample back to a NumPy array
            next_sample_fedformer = next_sample_fedformer.cpu().numpy()

            # Append the refined sample to the generated sequence
            generated_sequence = np.append(generated_sequence, next_sample_fedformer, axis=0)

    # Set the models back to training mode
    rave_model.train()
    fedformer_model.train()

    return generated_sequence