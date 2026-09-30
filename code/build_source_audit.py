"""Serialize the supplied 2026-09-30 code audit; no network or code execution."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER_LOCATIONS = {
 'arxiv-1609.02943':[2], 'arxiv-1909.01838':[16], 'arxiv-1910.00744':[],
 'arxiv-2003.04884':[1], 'eprint-2023-1526':[22], 'arxiv-2406.10011':[],
 'eprint-2026-296':[5], 'arxiv-2609.14379':[], 'eprint-2024-1403':[4],
 'eprint-2024-1580':[29], 'eprint-2025-1118':[19,20], 'eprint-2025-1868':[1,5],
 'eprint-2026-1164':[4], 'eprint-2026-139':[4], 'eprint-2026-241':[5],
 'eprint-2026-464':[28], 'eprint-2026-902':[], 'eprint-2025-1970':[5],
 'eprint-2026-178':[28,32], 'eprint-2026-253':[20], 'eprint-2026-1066':[],
 'eprint-2026-168':[], 'eprint-2026-719':[3], 'arxiv-2601.16873':[],
 'arxiv-2608.03294':[], 'eprint-2026-1678':[4], 'arxiv-2608.06631':[],
 'arxiv-2403.06634':[10,21], 'arxiv-2403.09539':[], 'eprint-2026-848':[6],
 'eprint-2024-1870':[3], 'arxiv-1810.09076':[], 'arxiv-2002.11021':[],
 'arxiv-2503.19142':[2,4,15], 'eprint-2026-1943':[3], 'arxiv-2509.16546':[13,14,17],
 'mit-2026-rounding':[], 'arxiv-1807.05185':[], 'arxiv-2105.09673':[],
 'arxiv-2211.04589':[], 'arxiv-2304.12794':[5,14], 'arxiv-2312.04675':[],
 'arxiv-2402.04084':[], 'arxiv-2411.07536':[], 'arxiv-2511.20312':[2],
 'arxiv-2508.15031':[1], 'arxiv-2506.22521':[], 'arxiv-2609.18751':[5],
 'eprint-2026-2127':[6], 'arxiv-2609.21941':[], 'arxiv-2609.27427':[4]
}
HASHES = '''arxiv-1609.02943 0140d9ab6257972ae5ce88b5d9ae8978b335083cb1c226e1b995da975d18a885
arxiv-1909.01838 b30e63fd43c3dbf8d9dee7dc8c30d250982c8c911367018f1a1ad084d446ed82
arxiv-1910.00744 5c073d3cb6c38fa993c2bb660948df722533984f5f232000052d23d66a139772
arxiv-2003.04884 ee7ba5bd8c3893ab172e5272e1d81f66806fdbdea296a3da9a34561eb323c656
eprint-2023-1526 bdcbb2a5e1de1b0eeec5618ac4b0086578071806187d8a972a8cfcb21082239f
arxiv-2406.10011 c385371255cbdc47f0ab82e748ad6fe707b50b9117f3feaa6feebf2349bd1ccd
eprint-2026-296 b3bdc1253cfcb6f217a32a5403b931c690982280ad9c48f8b6bf54c83f07d73e
arxiv-2609.14379 4f62618e85427fbfff5dfc00fc635001404204852a7147685397b5d5372ba452
eprint-2024-1403 ef85d32b23c0dc621d8249e0ed7e14f1a39ae11dd66997289379b2fe4d2ac4f8
eprint-2024-1580 0477e78329fd227b51735c0fe05bc19fd2e5aefe980a4b662f795d81157067a7
eprint-2025-1118 74fc73b26656671e7016455ff7de0a2d7c674b0586af1c87368940c8b9168231
eprint-2025-1868 4f932596ffdce2bbee20e11ef7991170969b650ca6de0fb31b3c63d6908291a7
eprint-2026-1164 0c95c64f994d6ab7ebea85eb77cb5c5f03edb073353192eaf9b6ba90ffea0547
eprint-2026-139 8821dcf1019b718cdd53da1594c04b53e1c702c5fbb169c58c11fa7f8de7ac5f
eprint-2026-241 3cde3403d6973aedd36eb83434746b815e0fb55cc440f64866273027fbef37ea
eprint-2026-464 6128c62c2def3827feb981a9f16105870c0e71a38dc876fd1cf504a766c5dfc5
eprint-2026-902 d65ddea75a3961dfd3b83e2fa5bdf1e9d3a0a090c17cc09db451e11ce92f778e
eprint-2025-1970 db9a8d51e1093083d3e200d3728c5b2c6a87a7673347e27835d8db62e38e52eb
eprint-2026-178 27557ffbae790abcba5b8a69a24adbcedd58bf07e32c9309ebe1fb184775f88b
eprint-2026-253 ebe4080c30a61c1ce1ca3a1699009c9a07b8194a57ffc2be7ebbab194d8eaf78
eprint-2026-1066 f771f5abd060140eed2c0e5daa7003ba2041cea03fcee7bb6aa28fc63d8a0335
eprint-2026-168 fc39c1f1ffb4c54c83d247b992e65def6b8885699ee3d74547e5fbc10f1a3c18
eprint-2026-719 b2791b2be9d9fde33c3fb8be5015442a8f922af40a6b162ccdb454ed3e21181c
arxiv-2601.16873 e5221682c1da801dbae06aa21ab2d8469839d49cba2f623ae12b770fbe5a76f8
arxiv-2608.03294 7d08f64a35f9d3b3268759a8ddd2199c32caaffd5195545dd920d57db25e5bc1
eprint-2026-1678 9dcc514494113a6c7135fbb594d364f0c00730c4f671011981b0e95b47ecf45d
arxiv-2608.06631 f2a72cd14354a5920165c014bb2f5f637bbfde0f2c111c9eda50c4ebdff797f7
arxiv-2403.06634 65e2ade24ecefc77ab5eaab511b744a611bbc7efd0ec9ad6d434a3f23003be3c
arxiv-2403.09539 a5a1d06963f2b2cf82faca2589417c5a4cb50f7fd5779b4ce60af1d22e410341
eprint-2026-848 9aba9810291a1478f03993fea74caf163dd1cdafb606635e8e0dbe3042a0d6d1
eprint-2024-1870 6864a3e9250cee35b85db003e52545fa9deedc8536b048b702a62c8ff12ef2aa
arxiv-1810.09076 5912cf57bd630325b9af898b680450de6c69b2e5ac43aa2f81f8242bd7fc9cba
arxiv-2002.11021 b4da32e135b1e19114f48c81797cc8bb24bd17738f317257ca02d6d8d02fa04c
arxiv-2503.19142 127dbe082ac0ca3a0e9549b254a4c88544ceebcb886a2b8a41abf23a8aa3ddaa
eprint-2026-1943 218e87337001ee029343e2395dc9066195460bd69269e9da9fd344dd873a36fa
arxiv-2509.16546 93ea74db23b07de5d76bcbe6c8d1c6bb5c53a43ec45d7829b89ec1cb34f8eea9
mit-2026-rounding 71c2e278e5b0a58509c44d1a3d63c29e85940cdc5a8ea791dd3a7f62889d65f4
arxiv-1807.05185 00f7ed79f1fc1bc747388969c08094a84a361f4111b277a20243f49e7c4ef1dd
arxiv-2105.09673 9dc8aca93a50168af5c3898b7c13645b048d89e18198c39b9a597b6ac94aa80b
arxiv-2211.04589 03a30b2fb844ff723cc24b8d6ebf54cb3a513e773dba71fe5faf729f33690e3b
arxiv-2304.12794 ff7a888a5b2774b6d7aa77097ab28400c48b579ae7e0bd3f3b9655b6e387b78f
arxiv-2312.04675 560f27fc825a389ff88b55239a52ade72454dd92e336294a966f55c54843c85b
arxiv-2402.04084 effb88320b0ec766311a3a3dd7995decbebd2ded8ff645cdd2a66ae89e3f5064
arxiv-2411.07536 f6178620d5d86f983258ad4abcdb0a287159e9acd6af9fdcc0c84fb2db8a7453
arxiv-2511.20312 5b388bf4bc4dcb99b13b2d7e22563f0a8a8f6a4b14c5a6a8848964d498dc142e
arxiv-2508.15031 b26663e14103465e6d9d0ce53acb0c3fbab28ef7be9b76600676c9b48e98a75b
arxiv-2506.22521 9deb5e321e741bdb653904175932a9b446a8105618050c3e0f726e89e8b6aeec
arxiv-2609.18751 975b97dbe759c8e80f44b96e84da0626c6bd056aa2cad50f26f88fc826f4760b
eprint-2026-2127 c7fe321aa1e708f81e1fc956bcb37411aabdcf122884b8307940a556515aac64
arxiv-2609.21941 23b82be460837123e7330a5fb1887e67e62bb2bad41515e3401f58416857f583
arxiv-2609.27427 f5525b59df0457e0bb268f1262df03e41139b883a5d10f076adfd3c1fb8ac4b3'''

REPO_ROWS = '''ftramer/Steal-ML master e37c67b2f74e42a85370ce431bc9d4e391b0ed8b implementation none 130
google-research/cryptanalytic-model-extraction master 1093b6212f7018b1c14e24c80edb56ac05c0777c implementation Apache-2.0 15
Crypto-TII/deti main e411fbc28225a7d627cf2eebd57a92812104bf2b implementation MIT 14
hannafoe/cryptanalytical-extraction main 4280cd6770560fa717e6e8b4d337a29ba8bba77c implementation none 53
PsyduckLiu/End-to-End-Deep-Neural-Network-Extraction main 5206db797c123136aad21f69e7e01aeb15c2d9e0 implementation MIT 61
1983321048/Geometric-Critical-Point-Screening main 595fce480e82dab009c185e41f233fc477a6cc15 implementation none 60
AI-Lab-Y/NN_cryptanalytic_extraction main f363700ff141a8e0f81c68fb18ce703897884fc5 verification_artifact MIT 93
Jchavezsaab/hard-label-dnn-extraction main 2a450eb5096d99cb8cf9ac99c00c13f721071890 implementation MIT 47
deividafonso281/hard-label-contract-output main 0d137df322000eb07d7082497e83f6c07d3f00a8 supplementary_implementation none 101
ECSIS-lab/hard-label-cross-layer-extraction none none unavailable unverified 0
czr-eric/Algebraic-Attack-on-CNN none none unavailable unverified 0
PsyduckLiu/Model-Extraction-of-CNNs-with-Max-Pooling main 56cb180d255df2a8d8af8766378b2ec490611d3a implementation none 26
AI-Lab-Y/Extracting_PReLU_NN main d724ce37dac9a119ec388f241a9341a7650785d7 implementation none 236
qixiaokang1-stack/cryptanalytic-model-various-functions main 2d3a9dbff314d620fe1e33ac09d0f84ae87149fb implementation none 2191
mstealercryptocrypto-ops/mod_stealer26 main 95a5cd29bc23f3ce38a99802e0c6e2891ce3ef2d implementation none 77
springli07/GNN_MP_CEA main dde7f7e529a39eaa219924a4ec11e2ceab37c6e7 implementation none 56
dpaleka/stealing-part-lm-supplementary main 6fa1d1a87b06e00228330711eb661cee58b4740d supplementary_implementation MIT 36
bcoqueret/Side_channel_cryptanalytic_extraction_of_DNN main 8a729158d83adf587e2d2444e6587a2f489603b9 simulation_artifact none 618
heavyimage/afch_paper main 1b5d035d1f13de4ded4c1e435de7301f16c3c983 implementation GPL-3.0 225
CryptAnalystDesigner/Finite-Precision-Feasibility-of-Cryptanalytic-Model-Extraction none none unavailable unverified 0
anonymous-123-code/anonymouscode main 2092c04718d81c69dfcba88702f0c6b6dcd70b3f implementation none 65
flavio-martinelli/expand-and-cluster main 231cac970ceef43cb6361cd39917d75e44d7776e implementation MIT 121
alexl4123/expand-and-cluster main 07edef32b213f7a56a1fd66249e6f6b8207aabbf author_extension_fork MIT 1357
kzhao5/ModelExtractionPapers main 8571dde8fede0a27064705348db78e22e4d9b1b7 reading_resource none 2
CryptoAiLi/DNNExtractionLAK master da4fa69cb63bd6868b786db70af455bec7b65344 placeholder_repository none 6'''

NOTES = {
 'ftramer/Steal-ML':'Legacy Python dependencies; some experiments require AWS/BigML accounts. Third-party libsvm COPYRIGHT does not license the whole repository.',
 'google-research/cryptanalytic-model-extraction':'Research implementation; accessibility and documentation audited, results not reproduced.',
 'Crypto-TII/deti':'Sign-recovery experiments; assumes prior signatures and float64. Parallelization described in paper is not fully implemented.',
 'hannafoe/cryptanalytical-extraction':'Layer-wise experiments; earlier layers treated as correct by default; CIFAR signature recovery not implemented. Incorporates other upstream code; no project-wide license located.',
 'PsyduckLiu/End-to-End-Deep-Neural-Network-Extraction':'README example enables cheat_sign=1 and real_attack=0; users must distinguish diagnostic modes from real attack. MIT root license does not settle licensing of reused third-party snippets.',
 '1983321048/Geometric-Critical-Point-Screening':'README prominently links CRYPTO 2020 ancestor rather than the new paper. Only rubbish/LICENSE found; no project-wide license established.',
 'AI-Lab-Y/NN_cryptanalytic_extraction':'README documents verification of stored extracted models/records and error bounds. Do not present it as a complete end-to-end attack implementation.',
 'Jchavezsaab/hard-label-dnn-extraction':'Root calls this supplementary code. full_end_to_end/run.py is documented as black-box; signature_recovery and sign_recovery demos explicitly use white-box shortcuts. Precomputed dual points are separately linked, not automatically downloaded.',
 'deividafonso281/hard-label-contract-output':'Supplementary layer-recovery experiments; incorporates deti functions.',
 'PsyduckLiu/Model-Extraction-of-CNNs-with-Max-Pooling':'Proof-of-concept CNN extraction; no project-wide license located.',
 'AI-Lab-Y/Extracting_PReLU_NN':'Research implementation; accessibility and documentation audited, results not reproduced.',
 'qixiaokang1-stack/cryptanalytic-model-various-functions':'README is named READEME.md. Some documented generic filenames differ from actual tree (e.g. ELU/end-to-end.py); verify paths manually. README reports unsuccessful HardTanh S5 end-to-end experiments.',
 'mstealercryptocrypto-ops/mod_stealer26':'Requires native backend compilation; no code/build executed. Experimental codebase; root README does not name the paper, provenance comes from paper PDF.',
 'springli07/GNN_MP_CEA':'Research implementation; accessibility and documentation audited, results not reproduced.',
 'dpaleka/stealing-part-lm-supplementary':'Local logit-query attack and API-emulation experiments, not the full production-model extraction pipeline. Old real-API behavior is explicitly obsolete.',
 'bcoqueret/Side_channel_cryptanalytic_extraction_of_DNN':'Notebooks simulate the side-channel oracle by directly accessing neuron states; no physical side-channel measurements reproduced. README uses a prior paper title.',
 'heavyimage/afch_paper':'Requires SGX-capable hardware, SGX-Step setup and native builds; review GPL and third-party/submodule obligations separately. No system changes performed.',
 'anonymous-123-code/anonymouscode':'Defense code built on Foerster et al. extraction; no project-wide license located.',
 'flavio-martinelli/expand-and-cluster':'Research implementation; accessibility and documentation audited, results not reproduced.',
 'alexl4123/expand-and-cluster':'Author-linked extension of flavio-martinelli/expand-and-cluster; keep distinct pinned checkout because changes implement a different paper.',
 'kzhao5/ModelExtractionPapers':'Bibliographic reading list shared by two survey entries; not attack code.',
 'CryptoAiLi/DNNExtractionLAK':'Pinned tree contains only .idea IDE metadata; no implementation, README or license found.'
}

COMMANDS = {
 'google-research/cryptanalytic-model-extraction':[
  'pip install numpy scipy jax jaxlib matplotlib networkx',
  'python3 train_models.py 10-15-15-1 42', 'python3 extract.py 10-15-15-1 42',
  'python3 check_solution_svd.py 10-15-15-1', 'python3 check_solution_milp.py 10-15-15-1',
  'python extract.py UID 20-10-1'],
 'Crypto-TII/deti':[
  "python -m deti.soe --model deti/models/unitary_784_128_1.keras --layerID 1 --runID 'soe'",
  "python -m deti.lastLayer --model deti/models/unitary_784_128_1.keras --layerID 1 --runID 'lastLayer'",
  "python -m deti.neuronWiggle --model deti/models/unitary_100_200x3_10.keras --layerID 1 --runID 'neuronWiggle' --tgtNeurons 4 26 30 77 168 ",
  "python -m deti.neuronWiggle --model deti/models/unitary_100_200x3_10.keras --layerID 2 --runID 'neuronWiggle' --tgtNeurons 4 26 30 77 168 ",
  "python -m deti.lastLayer --model deti/models/unitary_100_200x3_10.keras --layerID 3 --runID 'lastLayer'",
  "python -m deti.soe --model deti/models/cifar10_rgb_8x256.keras --layerID 1 --runID 'soe'",
  "python -m deti.neuronWiggle --model deti/models/cifar10_rgb_8x256.keras --layerID 2 --runID 'neuronWiggle' --dataset 'CIFAR10' --tgtNeurons 4 26 30 77 168 ",
  "python -m deti.lastLayer --model deti/models/cifar10_rgb_8x256.keras --layerID 8 --runID 'lastLayer'",
  'conda create -n tf-gpu tensorflow-gpu', 'conda activate tf-gpu', 'conda install -c nvidia cuda-nvcc',
  'conda install pandas', 'conda install tabulate', 'conda install numpy',
  "python -m deti.soe --model deti/models/cifar10_rgb_8x256.keras --layerID 2 --runID 'soe'",
  "python -m deti.neuronWiggle --model deti/models/cifar10_rgb_8x256.keras --layerID 2 --runID 'neuronWiggle'"],
 'hannafoe/cryptanalytical-extraction':[
  "python -m neuronWiggle --model models/mnist784_16x2_1.keras --layerID 2 --seed 20 --dataset 'mnist' --quantized 2",
  'python -m neuronWiggle --model models/50_25x2_1_Carlini.keras --layerID 2 --seed 20 --quantized 1',
  r'python .\models\make_new_models.py', 'pip install tensorflow==2.15.0', 'pip install numpy==1.25.2',
  'pip install pandas==2.1.2', 'pip install jax==0.4.30', 'pip install optax==0.2.3', 'pip install scipy==1.9.3'],
 'PsyduckLiu/End-to-End-Deep-Neural-Network-Extraction':[
  'python main.py --load_json scripts/attack/mnist/MNIST_8x8_1_linear.json --seed 42 --Count 3000 --layerID 2 --cheat_sign 1 --real_attack 0',
  'pip install -r requirements.txt', 'python models/train_new_models_tf.py --load_json &lt;config_file&gt; ',
  'python main.py --load_json &lt;config_file&gt; --seed &lt;random_seed&gt; --Count &lt;critical_point_number&gt; --layerID &lt;target_layer_id&gt; --cheat_sign &lt;0/1&gt; --real_attack &lt;0/1&gt;',
  'python visualization/unreachable_weights_test.py --load_json &lt;config_file&gt; --random_points_number &lt;random_point_number&gt;',
  'python visualization/compute_difference.py --seed &lt;random_seed&gt; --Count &lt;critical_point_number&gt; --delta &lt;random_input_point_number&gt; --load_json &lt;config_file&gt;'],
 '1983321048/Geometric-Critical-Point-Screening':[
  'pip install -r requirements.txt', 'pip install numpy scipy jax jaxlib optax matplotlib networkx',
  'pip install numpy scipy jax jaxlib optax matplotlib networkx tensorflow',
  'python train_models_mnist.py 784-64-64-1 42', 'python train_models_mnist.py 784-8-8-8-8-8-8-8-8-1 42',
  'python train_models_mnist.py 784-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-1 42',
  'python train_models_mnist.py 784-128-128-1 42', 'python train_models_mnist.py 784-256-256-1 42',
  'python train_models_cifar10.py 3072-8-8-8-8-8-8-8-8-1 42',
  'python Geometric_1.py &lt;network_architecture&gt; &lt;random_seed&gt;', 'python Geometric_1.py 784-8-8-8-8-8-8-8-8-1 42'],
 'Jchavezsaab/hard-label-dnn-extraction':['cd full_end_to_end &amp;&amp; python3 run.py [num workers]'],
 'deividafonso281/hard-label-contract-output':['python outputLayer.py 0'],
 'PsyduckLiu/Model-Extraction-of-CNNs-with-Max-Pooling':[
  'python -u main.py --load_json scripts/attack/VGG-tiny/args.json --layerID 1 --Count 1000 --noise_strategy 2 --efficient_weight_recovery 0',
  'python -u main.py --load_json scripts/attack/VGG-bad/args.json --layerID 3 --Count 200 --noise_strategy -1',
  'pip install -r requirements.txt', 'python models/train_new_models_tf.py --load_json &lt;config_file&gt; ',
  'python main.py --load_json &lt;config_file&gt; --layerID &lt;layer_number&gt; --Count &lt;critical_point_number&gt; --noise_strategy &lt;strategy_number&gt; --efficient_weight_recovery &lt;0,1&gt;'],
 'AI-Lab-Y/Extracting_PReLU_NN':[
  'python comparison.py d0-d1-d2 random_seed', 'python end-to-end-k-deep-extraction.py d0-d1-d2 random_seed',
  'python check_solution_svd d0-d1-d2', 'python end-to-end-k-deep-extraction.py d0-d1-d2 file_no topK random_seed',
  'python check_solution_svd d0-d1-d2 topK'],
 'qixiaokang1-stack/cryptanalytic-model-various-functions':[
  'python find_duals.py ARCHITECTURE SEED', 'python find_duals_layerwise.py ARCHITECTURE SEED',
  'python cluster_dual_points.py ARCHITECTURE SEED', 'python recover_weights.py ARCHITECTURE SEED',
  'python extract_end_to_end.py ARCHITECTURE SEED', 'python MNIST_end_to_end.py SEED',
  'python cluster_dual_points.py ARCHITECTURE SEED LAYER_INDEX', 'python recover_weights.py ARCHITECTURE SEED LAYER_INDEX',
  'python extract.py ARCHITECTURE SEED', 'python 1_batched_sign_recovery.py', 'python create_tables.py',
  'python additional_parameters_recover.py ARCHITECTURE SEED LAYER_INDEX', 'python step_recovery_S5.py ARCHITECTURE SEED',
  'python step_recovery_S1.py ARCHITECTURE SEED', 'python MNIST_step_recovery_S5.py', 'python MNIST_step_recovery_S1.py'],
 'springli07/GNN_MP_CEA':[
  'pip install -r requirements.txt', r'python .\train_target.py l4_h32_seed7', r'python .\train_target.py l4_h32_seed7 --dry-run',
  r'python .\recovery_pipeline\summarize_activation_regimes.py l4_h32_seed7 --num-samples 20000 --batch-size 512',
  r'python .\recovery_pipeline\find_duals.py l4_h32_seed7 2000', r'python .\recovery_pipeline\find_duals.py l4_h32_seed7 2000 --node 0,1',
  r'python .\recovery_pipeline\collect_duals_to_target.py l4_h32_seed7 160000',
  r'python .\recovery_pipeline\cluster_dual_points.py l4_h32_seed7 4', r'python .\recovery_pipeline\class_cluster_all.py l4_h32_seed7',
  r'python .\recovery_pipeline\recover_weights_v3.py 0 l4_h32_seed7 --prefix-mode auto --subsample-trials 4',
  r'python .\recovery_pipeline\recover_weights_v3.py 1 l4_h32_seed7 --prefix-mode auto --subsample-trials 4',
  r'python .\recovery_pipeline\recover_weights_v3.py 2 l4_h32_seed7 --prefix-mode auto --subsample-trials 4',
  r'python .\recovery_pipeline\recover_last_layer_refined.py l4_h32_seed7 --source all-duals --max-points-per-node 400 --batch-size 1024',
  r'python .\recovery_pipeline\compute_dual_budget.py l4_h32_seed7', r'python .\recovery_pipeline\summarize_cluster_coverage.py l4_h32_seed7',
  r'python .\recovery_pipeline\summarize_recovery.py l4_h32_seed7', r'python .\summarize_structure_generalization.py',
  r'python .\check_status.py l4_h32_seed7', r'python .\check_status.py l4_h32_seed7 --target-total-per-node 160000',
  r'python .\run.py train --structure l4_h32_seed7',
  r'python .\run.py activation-regimes --structure l4_h32_seed7 --num-samples 20000 --batch-size 512',
  r'python .\run.py duals-to-target --structure l4_h32_seed7 --target-total-per-node 160000',
  r'python .\run.py cluster --structure l4_h32_seed7 --max-layer 4', r'python .\run.py neuron --structure l4_h32_seed7',
  r'python .\run.py recover --structure l4_h32_seed7 --all-hidden --prefix-mode auto --subsample-trials 4',
  r'python .\run.py recover-last-layer --structure l4_h32_seed7 --source all-duals --max-points-per-node 400 --batch-size 1024',
  r'python .\run.py summarize --structure l4_h32_seed7', r'python .\run.py train --structure l5_h24_seed7',
  r'python .\run.py train --structure l5_h32_seed7', r'python .\run.py train --structure l6_h16_seed7',
  r'python .\recovery_pipeline\recover_weights_v3.py 4 l6_h16_seed7 --cluster-id 15 --prefix-mode auto --subsample-trials 16 --subsample-strategy diversity --diversity-target-points 512'],
 'bcoqueret/Side_channel_cryptanalytic_extraction_of_DNN':['python -m venv .venv', 'pip install -r requirements.txt'],
 'heavyimage/afch_paper':['python3 attack.py'],
 'anonymous-123-code/anonymouscode':[
  "python -u -m neuronWiggle --model models/mnist784_16x8_1_Seed42.keras --layerID 1 --seed 20 --dataset 'mnist' --quantized 2 2&gt;&amp;1 &gt; .\\results\\mnist784_16x8_1_Seed42.txt              ",
  "python -u -m neuronWiggle --model models/Secure_mnist784_16x8_1_Seed42.keras --layerID 1 --seed 20 --dataset 'mnist' --quantized 2 2&gt;&amp;1 &gt; .results\\Secure_mnist784_16x8_1_Seed42.txt",
  r'python .\models\make_new_models.py', 'pip install tensorflow==2.15.0', 'pip install numpy==1.25.2',
  'pip install pandas==2.1.2', 'pip install jax==0.4.30', 'pip install optax==0.2.3', 'pip install scipy==1.9.3'],
 'flavio-martinelli/expand-and-cluster':[
  'python EC.py', 'python EC.py train --default_hparams=mnist_lenet_20 --help',
  'python EC.py train --default_hparams=mnist_lenet_20',
  'python EC.py train --default_hparams=mnist_lenet_20 --batch_size=1024 --lr=0.8 --warmup_steps=10ep',
  'python EC.py extract --help', 'python EC.py lottery --help',
  'python EC.py lottery --default_hparams=cifar_resnet_20 --levels=3',
  'python EC.py lottery --default_hparams=cifar_resnet_20 --levels=3 --rewinding_steps=500it']
}
COMMANDS['alexl4123/expand-and-cluster'] = COMMANDS['flavio-martinelli/expand-and-cluster'].copy()

DEPENDENCIES = {
 'ftramer/Steal-ML':['binary-classifiers/requirements.txt', 'neural-nets/requirements.txt', 'regression/requirements.txt', 'trees/requirements.txt'],
 'hannafoe/cryptanalytical-extraction':['requirements.txt'],
 'PsyduckLiu/End-to-End-Deep-Neural-Network-Extraction':['requirements.txt'],
 '1983321048/Geometric-Critical-Point-Screening':['requirements.txt'],
 'PsyduckLiu/Model-Extraction-of-CNNs-with-Max-Pooling':['requirements.txt'],
 'mstealercryptocrypto-ops/mod_stealer26':['requirements.txt'], 'springli07/GNN_MP_CEA':['requirements.txt'],
 'dpaleka/stealing-part-lm-supplementary':['requirements.txt'],
 'bcoqueret/Side_channel_cryptanalytic_extraction_of_DNN':['requirement.txt'],
 'heavyimage/afch_paper':['app/nn_param_recovery/requirements.txt'],
 'anonymous-123-code/anonymouscode':['requirements.txt'], 'flavio-martinelli/expand-and-cluster':['requirements.txt'],
 'alexl4123/expand-and-cluster':['requirements.txt']
}

def build():
    catalog = json.loads((ROOT/'data/papers.json').read_text(encoding='utf-8'))
    hashes = dict(line.split() for line in HASHES.splitlines())
    paper_ids_by_repo = {}
    papers = []
    prior_overrides = {'arxiv-1910.00744':'not_found','eprint-2024-1403':'official',
                       'eprint-2026-139':'expired_410','eprint-2026-902':'anonymous_attachment',
                       'eprint-2026-1678':'not_found','eprint-2026-848':'anonymous_attachment'}
    status_changes = {'official':'author_linked_implementation','supplementary':'supplementary_implementation',
                      'expired_410':'anonymous_attachment_access_unverified',
                      'anonymous_attachment':'anonymous_attachment_access_unverified'}
    source_overrides = {
        'arxiv-1910.00744':'https://media.icml.cc/Conferences/ICML2020/v119/rolnick20a-supp.zip',
        'eprint-2026-1678':'https://anonymous.4open.science/r/End-to-End-Softmax-Attention-Extraction-632C'}
    for p in catalog['papers']:
        pid=p['id']
        prior=prior_overrides.get(pid,p['code']['status'])
        status=status_changes.get(prior,prior)
        if pid=='arxiv-1910.00744': status='publisher_supplement_access_unverified'
        if pid=='eprint-2024-1403': status='verification_artifact'
        if pid=='eprint-2025-1118': status='supplementary_implementation'
        if pid=='eprint-2024-1870': status='simulation_artifact'
        if pid=='eprint-2026-1678': status='anonymous_attachment_access_unverified'
        source=source_overrides.get(pid,p['code'].get('url'))
        repo=source.split('github.com/')[1].rstrip('/') if source and source.startswith('https://github.com/') else None
        row={'paper_id':pid,'title':p['title'],'paper_url':p['url'],'status':status,'repository_id':repo,'prior_status':prior}
        if not repo: row['source_url']=source
        if pid=='eprint-2026-1025':
            row['provenance']=[{'kind':'prior_catalog_provenance_not_freshly_reverified','url':p['url'],'checked':'2026-09-17'}]
        else:
            pdf=p['pdf_url']
            if pid in ('arxiv-2609.21941','arxiv-2609.27427'): pdf=f"https://arxiv.org/pdf/{pid.removeprefix('arxiv-')}v1"
            row['provenance']=[{'kind':'reviewed_paper_text','url':pdf,'pdf_sha256':hashes[pid],
                                'code_link_locations':[{'page':n} for n in PAPER_LOCATIONS[pid]]}]
        if repo:
            paper_ids_by_repo.setdefault(repo,[]).append(pid)
            if pid!='eprint-2026-2127' and status!='unavailable_404':
                row['provenance'].append({'kind':'pinned_repository_readme','repository_id':repo})
        if pid=='arxiv-1910.00744':
            row['provenance'].append({'kind':'publisher_link','url':'https://proceedings.mlr.press/v119/rolnick20a.html',
                'note':'Other Files link targets supplementary ZIP; HTTP 403 prevented content inspection.'})
        if status=='anonymous_attachment_access_unverified':
            row['provenance'].append({'kind':'access_check','url':source,'date':'2026-09-30',
                'note':'Current access unverified; no license or fixed revision claimed.'})
        papers.append(row)
    repositories=[]
    entrypoint_paths={
        'ftramer/Steal-ML':[], 'AI-Lab-Y/NN_cryptanalytic_extraction':['check_solution_svd.py','verify_1_deep_nn_attack.py','verify_2_deep_nn_attack.py'],
        'Jchavezsaab/hard-label-dnn-extraction':[], 'mstealercryptocrypto-ops/mod_stealer26':['model_stealer.py'],
        'dpaleka/stealing-part-lm-supplementary':[], 'kzhao5/ModelExtractionPapers':[], 'CryptoAiLi/DNNExtractionLAK':[]}
    for line in REPO_ROWS.splitlines():
        rid,branch,commit,kind,license_name,count=line.split()
        access='unavailable_404' if commit=='none' else 'accessible'
        row={'id':rid,'url':f'https://github.com/{rid}','paper_ids':paper_ids_by_repo[rid],
             'access':access,'default_branch':None if branch=='none' else branch,
             'commit':None if commit=='none' else commit,'kind':kind}
        if access=='unavailable_404':
            row['license']={'spdx_id':None,'status':'unverified','evidence_url':None}
            row['note']='Read-only GitHub repository API returned HTTP 404 on audit date; this does not prove deletion.'
        else:
            license_files=['LICENSE'] if license_name!='none' else []
            if rid=='ftramer/Steal-ML': license_files=['binary-classifiers/libsvm-3.20/COPYRIGHT']
            if rid=='1983321048/Geometric-Critical-Point-Screening': license_files=['rubbish/LICENSE']
            if rid=='dpaleka/stealing-part-lm-supplementary': license_files=['LICENSE.md']
            row['license']={'spdx_id':None if license_name=='none' else license_name,
                'status':'no_project_license_found' if license_name=='none' else 'declared_license_verified',
                'evidence_url':None if license_name=='none' else f'https://github.com/{rid}/blob/{commit}/{license_files[0]}',
                'license_files':license_files,'api_detected_spdx':None if license_name=='none' else license_name}
            row['note']=NOTES[rid]
            row['entrypoints_documented']=COMMANDS.get(rid,[])
            row['dependency_files']=[{'path':f,'url_template':'pinned_file'} for f in DEPENDENCIES.get(rid,[])]
            row['source_files_count']=int(count)
            row['tree_truncated']=False
            if rid in entrypoint_paths: row['entrypoint_paths']=entrypoint_paths[rid]
            row['evidence_templates']=['repository_metadata','pinned_tree']
            readme='README.md'
            if rid in ('google-research/cryptanalytic-model-extraction','1983321048/Geometric-Critical-Point-Screening'): readme='README'
            if rid=='qixiaokang1-stack/cryptanalytic-model-various-functions': readme='READEME.md'
            if rid=='CryptoAiLi/DNNExtractionLAK': readme=None; row['readme_url']=None
            row['readme_path']=readme
            if readme: row['readme_url_template']='pinned_file'
            if rid=='AI-Lab-Y/NN_cryptanalytic_extraction': row['dependency_summary']='README declares Python 3.7.0 and NumPy 1.21.5.'
            if rid=='Jchavezsaab/hard-label-dnn-extraction':
                row['additional_documentation']=[{'path':path,'url_template':'pinned_file'} for path in ['README.md','full_end_to_end/README.md','generators/README.md','sign_recovery/README.md','signature_recovery/README']]
                row['dependency_summary']='sign_recovery README lists numpy, pandas, matplotlib, tabulate and tensorflow.'
        repositories.append(row)
    summary={'papers':52,'unique_github_repositories':25,'accessible_github_repositories':22,
        'status_counts':{'author_linked_implementation':15,'not_found':18,'publisher_supplement_access_unverified':1,'verification_artifact':1,'supplementary_implementation':2,'unavailable_404':3,'announced':2,'anonymous_attachment_access_unverified':4,'simulation_artifact':1,'mentioned':1,'author_extension_fork':1,'reading_resource':2,'placeholder_repository':1},
        'declared_project_licenses':{'no_project_license_found':13,'Apache-2.0':1,'MIT':7,'unverified':3,'GPL-3.0':1}}
    audit={'schema_version':1,'checked':'2026-09-30',
        'scope':'All 52 distinct papers in current catalog; primary paper text and repository metadata/documentation inspection only. No upstream code execution, model queries, dependency installs, system changes, or scientific reproduction.',
        'summary':summary,
        'policy':{
            'default':'References plus opt-in pinned git submodule or clone pointers; no upstream code vendored or automatically executed.',
            'no_license':'Public visibility is not a redistribution license. Repository pointers are not a claim of permission to redistribute upstream code; no permission inferred from third-party license files or ancestry.',
            'permissive':'MIT/Apache-2.0 root licenses are candidates for redistribution with preserved notices and full third-party review, not automatic clearance.',
            'copyleft':'GPL artifact requires separate compliance review; clone/reference by default.',
            'execution':'Commands are upstream documentation, not validated recommendations; never execute during collection.',
            'anonymous':'No automatic clone without accessible stable source and explicit pin.'},
        'papers':papers,'repositories':repositories,
        'url_templates':{
            'repository_metadata':'https://api.github.com/repos/{repository_id}',
            'pinned_tree':'https://api.github.com/repos/{repository_id}/git/trees/{commit}?recursive=1',
            'pinned_commit':'https://github.com/{repository_id}/commit/{commit}',
            'pinned_file':'https://github.com/{repository_id}/blob/{commit}/{path}'},
        'template_note':'Expand URL templates with repository_id=id from each repository row and its fixed commit. A paper pinned_repository_readme provenance entry references that repository readme_path. Dependency and documentation paths use pinned_file. For papers with repository_id, source_url is the referenced repository url.'}
    from collections import Counter
    assert len(papers)==len({p['paper_id'] for p in papers})==52
    assert len(repositories)==len({r['id'] for r in repositories})==25
    assert sum(r['access']=='accessible' for r in repositories)==22
    assert Counter(p['status'] for p in papers)==summary['status_counts']
    assert Counter(r['license']['status'] if not r['license']['spdx_id'] else r['license']['spdx_id'] for r in repositories)==summary['declared_project_licenses']
    return audit

if __name__=='__main__':
    out=ROOT/'code/source-audit.json'
    out.write_text(json.dumps(build(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Saved complete structured code audit: 52 unique papers, 25 repositories, 22 accessible repositories.')
