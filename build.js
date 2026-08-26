const { execSync } = require('child_process');

console.log('Generating lessons...');
try {
  execSync('node /Users/thanojbuddhima/.gemini/antigravity-ide/brain/c2589f53-b147-476f-80cd-b42b3c1e3b41/scratch/gen_batchA.js', { stdio: 'inherit' });
  execSync('node /Users/thanojbuddhima/.gemini/antigravity-ide/brain/c2589f53-b147-476f-80cd-b42b3c1e3b41/scratch/gen_batchB.js', { stdio: 'inherit' });
  execSync('node /Users/thanojbuddhima/.gemini/antigravity-ide/brain/c2589f53-b147-476f-80cd-b42b3c1e3b41/scratch/gen_batchC.js', { stdio: 'inherit' });
  execSync('node /Users/thanojbuddhima/.gemini/antigravity-ide/brain/c2589f53-b147-476f-80cd-b42b3c1e3b41/scratch/gen_batchD.js', { stdio: 'inherit' });
  execSync('node /Users/thanojbuddhima/.gemini/antigravity-ide/brain/c2589f53-b147-476f-80cd-b42b3c1e3b41/scratch/gen_batchE.js', { stdio: 'inherit' });
  execSync('node /Users/thanojbuddhima/.gemini/antigravity-ide/brain/c2589f53-b147-476f-80cd-b42b3c1e3b41/scratch/gen_batchF.js', { stdio: 'inherit' });
  execSync('node /Users/thanojbuddhima/.gemini/antigravity-ide/brain/c2589f53-b147-476f-80cd-b42b3c1e3b41/scratch/gen_batchG.js', { stdio: 'inherit' });
  execSync('node /Users/thanojbuddhima/.gemini/antigravity-ide/brain/c2589f53-b147-476f-80cd-b42b3c1e3b41/scratch/gen_index.js', { stdio: 'inherit' });
  
  console.log('\nPatching next lesson links...');
  execSync('node /Users/thanojbuddhima/.gemini/antigravity-ide/brain/c2589f53-b147-476f-80cd-b42b3c1e3b41/scratch/patch_links.js', { stdio: 'inherit' });
  
  console.log('\nBuild complete! All 45 lessons generated and linked.');
} catch (error) {
  console.error('Build failed:', error);
}
